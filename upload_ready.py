#!/usr/bin/env python3
"""Upload a finished (already edited) Crayon Babies video to YouTube.

Usage: python3 upload_ready.py jobs/<file>.json [--dry-run]

Job keys:
  video        path of the mp4 inside this repo (e.g. "ready/2026-10-28-sunny-cant-roar.mp4")
  title, description, tags, playlist
  publish_at   optional RFC3339 UTC time ("2026-10-28T18:53:00Z"). The video is uploaded as private and
               YouTube makes it public at that time. If the time has already passed, it is uploaded public now.
  thumbnail    optional path of a 1280x720 JPG (< 2 MB) inside this repo - set as the custom thumbnail
               (long videos; made with `compile.py thumb`)
  short        optional, default true; false for long videos (only changes the logged link format)

Channel rules: Made for kids, altered/synthetic (AI) = yes, NO hashtags added to the description.
Exit codes: 0 ok, 2 bad input, 4 API error.
"""
import datetime, json, sys
from pathlib import Path

import pipeline as P


def build_meta(job):
    now = datetime.datetime.now(datetime.timezone.utc)
    status = {"privacyStatus": "public", "selfDeclaredMadeForKids": True,
              "containsSyntheticMedia": True, "embeddable": True}
    when = job.get("publish_at")
    if when:
        at = datetime.datetime.fromisoformat(when.replace("Z", "+00:00"))
        if at > now + datetime.timedelta(minutes=15):
            status.update(privacyStatus="private", publishAt=at.strftime("%Y-%m-%dT%H:%M:%SZ"))
    tags = [t.lstrip("#") for t in job.get("tags", [])]
    snippet = {"title": job["title"][:100], "description": job["description"][:5000], "tags": tags,
               "categoryId": "1", "defaultLanguage": "en", "defaultAudioLanguage": "en"}
    return {"snippet": snippet, "status": status}


def set_thumbnail(token, vid, path):
    code, body, _ = P.http(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}&uploadType=media",
                           Path(path).read_bytes(), {"Authorization": f"Bearer {token}", "Content-Type": "image/jpeg"},
                           "POST")
    print(f"[thumbnail] HTTP {code}" + ("" if code == 200 else f": {body[:300]!r}"))


def upload(video, meta, playlist, thumbnail=None):
    token = P.yt_token()
    auth = {"Authorization": f"Bearer {token}"}
    size = video.stat().st_size
    code, body, headers = P.http(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status", meta,
        {**auth, "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)})
    loc = {k.lower(): v for k, v in headers.items()}.get("location")
    if code != 200 or not loc:
        raise RuntimeError(f"YouTube upload init HTTP {code}: {body[:400]!r}")
    code, body, _ = P.http(loc, video.read_bytes(), {**auth, "Content-Type": "video/mp4"}, "PUT")
    if code not in (200, 201):
        raise RuntimeError(f"YouTube upload HTTP {code}: {body[:400]!r}")
    vid = json.loads(body)["id"]
    # videos.insert can drop containsSyntheticMedia, so set the status again explicitly.
    code, body, _ = P.http("https://www.googleapis.com/youtube/v3/videos?part=status",
                           {"id": vid, "status": meta["status"]}, auth, "PUT")
    if code != 200:
        print(f"[status] update HTTP {code}: {body[:300]!r}")
    if thumbnail:
        try:
            set_thumbnail(token, vid, thumbnail)
        except Exception as e:
            print(f"[thumbnail] skipped: {e}")
    try:
        P.add_to_playlist(token, vid, playlist)
    except Exception as e:
        print(f"[playlist] skipped: {e}")
    code, body, _ = P.http(f"https://www.googleapis.com/youtube/v3/videos?part=status,snippet&id={vid}", headers=auth)
    st = json.loads(body)["items"][0]["status"] if code == 200 else {}
    print(f"[check] privacy={st.get('privacyStatus')} publishAt={st.get('publishAt')} "
          f"madeForKids={st.get('selfDeclaredMadeForKids')} synthetic={st.get('containsSyntheticMedia')}")
    return vid, st


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    job_path = Path(sys.argv[1])
    job = json.loads(job_path.read_text())
    video = (P.ROOT / job["video"]).resolve()
    if not video.is_file():
        print(f"ERROR: video not found: {video}")
        return 2
    meta = build_meta(job)
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    if "--dry-run" in sys.argv:
        return 0
    entry = {"time": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
             "idea": job.get("idea"), "title": job.get("title"), "file": job["video"],
             "viewmax_credits_used": job.get("viewmax_credits_used"), "status": "started"}
    try:
        thumb = (P.ROOT / job["thumbnail"]) if job.get("thumbnail") else None
        vid, st = upload(video, meta, job.get("playlist", "Crayon Babies Songs"), thumb)
        url = f"https://youtube.com/shorts/{vid}" if job.get("short", True) else f"https://www.youtube.com/watch?v={vid}"
        entry.update(status="uploaded", youtube_id=vid, url=url, kind="short" if job.get("short", True) else "long",
                     job=str(job_path), privacy=st.get("privacyStatus"), publish_at=st.get("publishAt"))
        print(f"[upload] {url}")
        P.log(entry)
        return 0
    except Exception as e:
        entry.update(status="failed", error=str(e))
        P.log(entry)
        print(f"ERROR: {e}")
        return 4


if __name__ == "__main__":
    sys.exit(main())
