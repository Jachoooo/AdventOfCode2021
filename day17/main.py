import time
import numpy as np
from numpy import product


FILENAME="test.txt"
if 0:
    xmin=20
    xmax=30
    ymin=-10
    ymax=-5
else:
    xmin=217
    xmax=240
    ymin=-126
    ymax=-69
starttime=time.perf_counter()

pairs=set()
print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    for line in file:
        for pair in line.split():
            x=int(pair.split(',')[0])
            y=int(pair.split(',')[1])
            pairs.add((x,y))


startpos=(0,0)
startvel=(21,10)

def updateVelPos(pos,vel):

    px=pos[0]+vel[0]
    py=pos[1]+vel[1]
    if vel[0]!=0:
        vx=int((vel[0]/abs(vel[0]))*(abs(vel[0])-1))
    else: vx=0
    vy=vel[1]-1
    return (px,py),(vx,vy)


res1=0
for y in range(260):

    p=startpos
    v=(21,y)
    temp=0
    for i in range(260):
        p,v=updateVelPos(p,v)
        
        
        if p[1]>temp:temp=p[1]
        if p[0]>=xmin and p[0]<=xmax and p[1]>=ymin and p[1]<=ymax:
            print(p,'\t',temp,'\t',y,'\t',i)
            print('HIT!')
            if temp>res1:res1=temp
            break

res2=set()
for x in range(1,xmax+1):
    for y in range(-150,150):
        p=startpos
        v=(x,y)
        v0=(x,y)
        
        for i in range(10000):
            p,v=updateVelPos(p,v)
            if p[0]>xmax or p[1]<ymin:
                break
            
            if p[0]>=xmin and p[0]<=xmax and p[1]>=ymin and p[1]<=ymax:
                res2.add(v0)
                
                break


print(f"\nPart 1 result = {res1}") 

print(f"Part 2 result = {len(res2)}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
