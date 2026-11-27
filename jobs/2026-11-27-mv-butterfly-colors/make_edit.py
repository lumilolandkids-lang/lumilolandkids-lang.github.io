# Builds edit.json for "Wow! A Red Butterfly! Colors Song" from the song timeline.
import json
CLIP=7.29
# song sections (seconds, from the assembled song.mp3: see song.txt)
S=[('hook',0,4.42),('chorus1',4.42,21.5),('red',21.5,36.9),('yellow',36.9,51.9),('chorus2',51.9,68.98),
   ('blue',68.98,84.0),('green',84.0,99.58),('clapbreak',99.58,112.9),('review',112.9,121.9),('answer',121.9,129.98),
   ('final',129.98,147.05),('outro',147.05,160.12)]
# pieces per section: (shot, start, dur, extra) ; the last dur of a section is fitted to the section end
P={
'hook':[(1,0.2,1.2,{'speed':0.85,'push':[1.0,1.06]}),(1,1.5,None,{'push':[1.0,1.08]})],
'chorus1':[(2,0.2,3.4,{}),(3,0.4,3.6,{}),(1,4.0,3.0,{'zoom':1.12}),(2,3.6,3.4,{'zoom':1.12}),(3,5.3,1.9,{}),(1,2.6,None,{'zoom':1.2})],
'red':[(4,0.1,3.4,{}),(4,3.6,3.0,{'zoom':1.1,'y':0.3}),(1,3.0,1.6,{'zoom':1.2}),(4,1.5,1.8,{'zoom':1.18}),(5,0.3,None,{})],
'yellow':[(6,0.1,3.8,{}),(6,5.0,2.2,{'zoom':1.1}),(6,0.4,3.4,{'zoom':1.2,'x':0.6}),(6,1.0,2.8,{'zoom':1.35,'x':0.7}),(6,0.2,None,{'zoom':1.15})],
'chorus2':[(3,0.4,3.0,{}),(2,0.3,3.0,{'zoom':1.1}),(5,0.6,2.8,{}),(3,5.3,1.9,{}),(2,3.8,3.0,{}),(1,3.6,None,{'zoom':1.1})],
'blue':[(7,0.1,3.3,{}),(7,3.5,3.0,{'zoom':1.1}),(7,0.8,2.6,{'zoom':1.2,'y':0.3}),(7,1.8,2.8,{'zoom':1.3,'x':0.7}),(7,3.8,None,{'zoom':1.15})],
'green':[(8,0.1,3.4,{}),(8,3.6,3.0,{}),(8,1.0,2.6,{'zoom':1.2,'y':0.3}),(8,5.2,2.0,{}),(8,2.2,None,{'zoom':1.12})],
'clapbreak':[(2,0.1,2.8,{}),(9,0.2,3.2,{}),(7,0.6,2.6,{}),(9,3.6,2.4,{'zoom':1.1}),(2,4.0,None,{'zoom':1.1})],
'review':[(9,0.4,2.0,{'zoom':1.1}),(10,0.1,1.5,{'push':[1.0,1.08]}),(10,2.4,3.0,{'speed':1.25,'push':[1.0,1.12]}),(10,3.9,None,{'push':[1.1,1.25]})],
'answer':[(11,1.0,3.0,{}),(11,4.1,3.0,{'zoom':1.08}),(11,1.8,None,{'zoom':1.2})],
'final':[(9,0.2,3.0,{}),(3,0.4,3.0,{}),(9,3.4,2.8,{'zoom':1.1}),(11,1.2,2.6,{}),(2,0.6,2.8,{}),(9,0.6,None,{'zoom':1.15})],
'outro':[(12,0.1,3.4,{}),(12,3.6,3.5,{'zoom':1.08}),(4,0.4,3.0,{}),(12,0.4,None,{'push':[1.0,1.1]})],
}
cuts=[]; marks={}
for name,a,b in S:
    t=a; marks[name]=len(cuts)
    for i,(sh,st,d,ex) in enumerate(P[name]):
        last=(i==len(P[name])-1)
        sp=ex.get('speed',1.0)
        if last: d=round((b-t)*sp,3)
        if st+d>CLIP-0.05: print(f'!! {name}: shot{sh} {st}+{d:.2f} > clip')
        c={'shot':sh,'start':st,'dur':round(d,3)}; c.update(ex); cuts.append(c); t+=d/sp
print('total %.2f'%t)
json.dump(marks,open('marks.json','w'))
edit={'workdir':'runs/2026-11-27-mv-butterfly-colors','out':'final.mp4','song':'song.mp3','song_start':0.0,'size':[1920,1080],
 'bounce':{'amp':0.03,'ranges':[[4.6,21.4],[52.0,68.9],[99.6,112.8],[130.0,147.0]]},
 'cuts':cuts,'sfx':[],'vfx':[]}
json.dump(edit,open('edit_base.json','w'),indent=1)
print(len(cuts),'cuts')

# ---- effects (absolute times) ----
edit['vfx']=[
 {'type':'sparkle','t':0.1,'x':0.82,'y':0.36,'size':0.6,'arc':[-70,70],'flash':False},
 {'type':'sparkle','t':21.6,'x':0.83,'y':0.42,'size':0.7,'arc':[-60,60]},
 {'type':'sparkle','t':37.0,'x':0.71,'y':0.6,'size':0.7,'arc':[-60,60]},
 {'type':'sparkle','t':69.1,'x':0.76,'y':0.27,'size':0.7,'arc':[-60,60]},
 {'type':'sparkle','t':84.1,'x':0.70,'y':0.39,'size':0.7,'arc':[-60,60]},
 {'type':'confetti','t':104.5,'dur':2.4,'keep_out':[0.5,0.4,0.25,0.4]},
 {'type':'sparkle','t':122.0,'x':0.64,'y':0.44,'size':0.8,'arc':[-60,60]},
 {'type':'confetti','t':122.1,'dur':2.6,'keep_out':[0.42,0.4,0.25,0.42]},
 {'type':'confetti','t':130.1,'dur':2.4,'keep_out':[0.5,0.4,0.25,0.4]},
 {'type':'hearts','t':147.3,'x':0.15,'y':0.9},
 {'type':'hearts','t':147.5,'x':0.85,'y':0.9},
]
def cut_at(t):
    acc=0
    for i,c in enumerate(edit['cuts']):
        d=c['dur']/c.get('speed',1.0)
        if acc+d>t: return i, t-acc
        acc+=d
fx=[('sfx/sparkle_chime.mp3',0.1,0.5,1.0),('sfx/pop.mp3',21.6,0.45,0.6),('sfx/pop.mp3',37.0,0.45,0.6),
    ('sfx/pop.mp3',69.1,0.45,0.6),('sfx/pop.mp3',84.1,0.45,0.6),
    ('sfx/question_boing.mp3',119.3,0.55,0.62),('sfx/toddlers_cheer_clap.mp3',122.0,0.5,2.1)]
for f,t,v,mx in fx:
    i,o=cut_at(t); edit['sfx'].append({'file':f,'cut':i,'offset':round(o,3),'vol':v,'max':mx})
json.dump(edit,open('edit.json','w'),indent=1)
print('effects', len(edit['vfx']), len(edit['sfx']))
