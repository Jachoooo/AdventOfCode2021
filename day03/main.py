#Advent of Code 2021
#JKL
import time
import numpy as np
from numpy.lib.function_base import average
FILENAME="input.txt"
starttime=time.time()

#Part 1
inputFile=open(FILENAME,'r')
H=0
arr=[]
for line in inputFile:
    L=len(line.strip())
    for c in line.strip():
        arr.append(int(c))
    H+=1
inputFile.close()

arr=np.array(arr).reshape((H,L))
arr=np.round(np.mean(arr,axis=0)).astype(int).astype(str)

gamma=''
epsilon=''
rev={'0':'1','1':'0'}
for c in arr:
    gamma+=c
    epsilon+=rev[c]
gamma=int(gamma,base=2)
epsilon=int(epsilon,base=2)
print("\neps =",epsilon)
print("gam =",gamma)

print("Part1 result =",epsilon*gamma,"\n")

#Part 2

inputFile=open(FILENAME,'r')
H=0
arr=[]
for line in inputFile:
    L=len(line.strip())
    for c in line.strip():
        arr.append(int(c))
    H+=1
inputFile.close()

arr=np.array(arr).reshape((H,L))
#print(arr)
arr2=np.copy(arr)

for i in range(arr.shape[1]):
    mn=np.mean(arr[:,i])
    rn=np.round(mn).astype(int)
    if mn == 0.5 : rn = 1
    arr=np.delete(arr,arr[:,i]!=rn,0)

OxR=''
for c in arr[0].astype(str):
    OxR+=c
print("OxR =",OxR:=int(OxR,base=2))

for i in range(arr2.shape[1]):
    mn=np.mean(arr2[:,i])
    rn=np.round(mn).astype(int)
    if mn == 0.5 : rn = 1
    if np.delete(arr2,arr2[:,i]==rn,0).size==0:break
    arr2=np.delete(arr2,arr2[:,i]==rn,0)
    #print(arr2.size)

CsR=''
for c in arr2[0].astype(str):
    CsR+=c
print("CsR =",CsR:=int(CsR,base=2))

print("Part2 result =",CsR*OxR,"\n")
print("Done in {:.6f} s".format(time.time()-starttime))