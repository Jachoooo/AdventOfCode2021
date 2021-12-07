import time
import numpy as np
FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()
   


print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')
nums=[int(x) for x in inputFile.readline().strip().split(',')]



nums=np.array(nums)
print("Part 1 result =",np.sum(np.abs(nums-int(np.median(nums)))))



p2=10000000000000
for i in range(min(nums),mx:=max(nums)+1):
    if not i%100:print('[',int(i*100/mx),'%\t]',p2)    
    res=0
    for num in np.abs(nums-i):
        res+=int(num*(num+1)/2)
    p2=min(p2,res)
    
print("Part 2 result =",p2)
print("Done in {:.6f} s".format(time.time()-starttime))