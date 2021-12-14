import time
from copy import copy

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()



def expand(chars,step):
    
    b=chardict[chars]    
    numdict[b]+=1    
    if step>1:
        expand(chars[0]+b,step-1)
        expand(b+chars[1],step-1)

# PART 1
chardict={}
numdict={}
temp=set()
print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    startword=file.readline().strip()
    file.readline()
    for line in file:
        key,val=line.strip().split(' -> ')
        chardict[key]=val

for c in startword:
    temp.add(c)
for c in chardict.values():
    temp.add(c)
for key in chardict.keys():
    temp.add(key[0])
    temp.add(key[1])

for elem in temp:
    numdict[elem]=0

for c in startword:
    numdict[c]+=1


STEP=10
for a,b in zip(startword[:-1],startword[1:]):
    expand(a+b,STEP)

res1=max(numdict.values())-min(numdict.values())

#PART 2
paircnt={}
pairdict={}

for key in chardict.keys():
    paircnt[key]=0
for key in chardict.keys():
    pairdict[key]=[key[0]+chardict[key],chardict[key]+key[1]]

for a,b in zip(startword[:-1],startword[1:]):
    paircnt[a+b]+=1



for key in numdict:
    numdict[key]=0

for c in startword:
    numdict[c]+=1

STEP=40
while STEP > 0 :
    temp=copy(paircnt)
    for key in chardict.keys():
        val=paircnt[key]
        temp[pairdict[key][0]]+=val
        temp[pairdict[key][1]]+=val
        temp[key]-=val   
        numdict[chardict[key]]+=val
    paircnt=temp
    STEP-=1

res2=max(numdict.values())-min(numdict.values())


    
print(f"Part 1 result = {res1}")     
print(f"Part 2 result = {res2}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
