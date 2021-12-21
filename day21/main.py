import time
from collections import Counter
import numpy as np
starttime=time.perf_counter()

FILENAME="input.txt"
D=False

P1score=0
P2score=0
P1pos=5
P2pos=6

class dice:
    itercount=0
    def __iter__(self):
        self.a = 1
        return self 
    def __next__(self):
        x = self.a
        self.itercount+=1
        if x < 100:
            self.a += 1
        else:
            self.a = 1
        return x
    

dice=dice()
dice=iter(dice)

while P1score<1000 and P2score<1000:

    P1pos=(next(dice)+next(dice)+next(dice)+P1pos)%10
    P2pos=(next(dice)+next(dice)+next(dice)+P2pos)%10

    #if P1pos==0:
    #    P1score+=10
    #else: 
    P1score+=P1pos+1

    if P1score>=1000: break

    
    P2score+=P2pos+1
    print(f'[P1] {P1pos}, {P1score}   [P2] {P2pos}, {P2score}')

a=dice.itercount-3
b=P2score

#Part 2 ########################################################


results=[]
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            results.append(i+j+k)
Nresults=np.array(results)

Npositions=np.arange(10)

Cnt=Counter(results)

Nresults=np.array([[3,4,5,6,7,8,9],[1,3,6,7,6,3,1]])

Ntransfer1=np.zeros((10,10,11,11,10,10),dtype=np.uint64)
Ntransfer2=np.zeros((10,10,11,11,10,10),dtype=np.uint64)

for tPos1 in range(10):
    for tPos2 in range(10):

        for t in np.rot90(Nresults):
            score=t[0]
            freq=t[1]
            trPos1=(score+tPos1)%10
            tScore1=trPos1+1
            Ntransfer1[tPos1,tPos2,tScore1,0,trPos1,tPos2]+=freq

for tPos1 in range(10):
    for tPos2 in range(10):

        for t in np.rot90(Nresults):
            score=t[0]
            freq=t[1]
            trPos2=(score+tPos2)%10
            tScore2=trPos2+1
            Ntransfer2[tPos1,tPos2,0,tScore2,tPos1,trPos2]+=freq
        

Nscore=np.zeros((41,41,10,10),dtype=np.uint64) #P1score,P2Score,P1position,P2position

P1pos=5
P2pos=6
Nscore[0,0,P1pos,P2pos]=1

res1=0
res2=0

Iters=22
for i in range(Iters):
    print(int(i*100/22),'%')
    temp=np.zeros((41,41,10,10),dtype=np.uint64)
    for Is1 in range(22):
        for Is2 in range(22):
            for Ip1 in range(10):
                for Ip2 in range(10):
                    if Nscore[Is1,Is2,Ip1,Ip2]==0:continue
                    temp[Is1:Is1+11,Is2:Is2+11,:,:]+=Ntransfer1[Ip1,Ip2,:,:,:,:]*Nscore[Is1,Is2,Ip1,Ip2]
    Nscore=temp
    res1+=np.sum(Nscore[21:,:,:,:])
    Nscore[21:,:,:,:]=0
    
    
    
    
    temp=np.zeros((41,41,10,10),dtype=np.uint64)
    for Is1 in range(22):
        for Is2 in range(22):
            for Ip1 in range(10):
                for Ip2 in range(10):
                    if Nscore[Is1,Is2,Ip1,Ip2]==0:continue
                    temp[Is1:Is1+11,Is2:Is2+11,:,:]+=Ntransfer2[Ip1,Ip2,:,:,:,:]*Nscore[Is1,Is2,Ip1,Ip2]
    Nscore=temp
    res2+=np.sum(Nscore[:,21:,:,:])
    Nscore[:,21:,:,:]=0

    
    
    

print(f"\nPart 1 result = {a*b}")
print(f"\nPart 1 result = {int(max(res1,res2))}")  

print("Done in {:.6f} s".format(time.perf_counter()-starttime))