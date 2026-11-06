#!/usr/bin/env python3
"""Weekly channel snapshot for the one-month test (her decision 6 Nov 2026, review on 6 Dec 2026).

Usage: python3 stats.py            -> appends one line to log/stats.jsonl and prints a short summary
Records channel views/subscribers/videos and views per video (id, title, kind, views, days online).
Baseline 6 Nov 2026: 191 views, 1 subscriber, 24 videos. Never prints secrets.
"""
import datetime, json
from pathlib import Path
import pipeline as P

API = "https://www.googleapis.com/youtube/v3"


def secs(iso):
    import re
    h, m, s = (re.search(r"(\d+)" + u, iso) for u in "HMS")
    return sum(int(x.group(1)) * k for x, k in ((h, 3600), (m, 60), (s, 1)) if x)


def get(url, auth):
    code, body, _ = P.http(url, headers=auth)
    if code != 200:
        raise SystemExit(f"HTTP {code}: {body[:300]!r}")
    return json.loads(body)


def main():
    auth = {"Authorization": f"Bearer {P.yt_token()}"}
    ch = get(f"{API}/channels?part=statistics,contentDetails&mine=true", auth)["items"][0]
    up = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], ""
    while True:
        b = get(f"{API}/playlistItems?part=contentDetails&maxResults=50&playlistId={up}{token}", auth)
        ids += [i["contentDetails"]["videoId"] for i in b["items"]]
        if not b.get("nextPageToken"):
            break
        token = f"&pageToken={b['nextPageToken']}"
    now = datetime.datetime.now(datetime.timezone.utc)
    vids = []
    for i in range(0, len(ids), 50):
        for v in get(f"{API}/videos?part=snippet,statistics,contentDetails&id={','.join(ids[i:i + 50])}", auth)["items"]:
            pub = datetime.datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z", "+00:00"))
            dur = v["contentDetails"]["duration"]
            vids.append({"id": v["id"], "title": v["snippet"]["title"][:80], "views": int(v["statistics"].get("viewCount", 0)),
                         "kind": "long" if secs(dur) > 70 else "short",
                         "days": round((now - pub).total_seconds() / 86400, 1)})
    s = ch["statistics"]
    snap = {"time": now.isoformat(timespec="seconds"), "views": int(s["viewCount"]), "subscribers": int(s["subscriberCount"]),
            "videos": int(s["videoCount"]), "per_video": sorted(vids, key=lambda x: -x["views"])}
    Path("log").mkdir(exist_ok=True)
    with open("log/stats.jsonl", "a") as f:
        f.write(json.dumps(snap, ensure_ascii=False) + "\n")
    longs = [v for v in vids if v["kind"] == "long"]
    print(f"[stats] views {snap['views']} (baseline 191 on 6 Nov) | subscribers {snap['subscribers']} | videos {snap['videos']}")
    print("[stats] top 5: " + " | ".join(f"{v['views']} {v['title'][:40]}" for v in snap["per_video"][:5]))
    print("[stats] long videos: " + " | ".join(f"{v['views']} views in {v['days']} d – {v['title'][:40]}" for v in longs))


if __name__ == "__main__":
    main()
