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

print("Part1 result =",epsilon*gamma)

#Part 2





print("Done in {:.6f} s".format(time.time()-starttime))