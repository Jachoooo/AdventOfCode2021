import time
import numpy as np
from PIL import Image
FILENAME="input.txt"

if FILENAME=="test.txt":
    D=True 
    SIZE=10
else:
    D=False
    SIZE=1000
starttime=time.time()



print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')
Coords=[]
for line in inputFile:
    Coords.append([int(y) for x in line.strip().split(' -> ') for y in x.split(',')])
inputFile.close()

if D:[print(Coord) for Coord in Coords]




#Part 1
diagram=np.zeros([SIZE,SIZE],dtype=int)
for line in Coords:
    if line[0] == line[2]:
        start = min(line[1],line[3])
        stop = max(line[1],line[3])+1
        diagram[start:stop,line[0]]+=1
    elif line[1] == line[3]:
        start = min(line[0],line[2])
        stop = max(line[0],line[2])+1
        diagram[line[1],start:stop]+=1
    else:
        continue

#Part 2
diagram2=np.zeros([SIZE,SIZE],dtype=int)
for line in Coords:
    if line[0] == line[2]:
        start = min(line[1],line[3])
        stop = max(line[1],line[3])+1
        diagram2[start:stop,line[0]]+=1
    elif line[1] == line[3]:
        start = min(line[0],line[2])
        stop = max(line[0],line[2])+1
        diagram2[line[1],start:stop]+=1
    else:
        x=line[0]
        if line[0]<line[2]:
            dx=1 
        else:
            dx=-1 
        y=line[1]
        if line[1]<line[3]:
            dy=1 
        else:
            dy=-1 
        while True:
            diagram2[y,x]+=1
            if x == line[2] : break
            x+=dx
            y+=dy

        
if D:print(diagram2)
print('Part 1 result =',np.sum(diagram>1))
print('Part 2 result =',np.sum(diagram2>1))
print("Done in {:.6f} s".format(time.time()-starttime))

mx=100/np.max(diagram)
img=Image.fromarray(255-(diagram*mx+(diagram>1)*155))
img=img.convert('RGB')
img.save('part1.png',bitmap_format='png')
mx=100/np.max(diagram2)
img=Image.fromarray(255-(diagram2*mx+(diagram2>1)*155))
img=img.convert('RGB')
img.save('part2.png',bitmap_format='png')