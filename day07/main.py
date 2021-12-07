import time
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()
#webbrowser.open('https://www.youtube.com/watch?v=LDU_Txk06tM',new=1)


print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')
nums=[int(x) for x in inputFile.readline().strip().split(',')]



nums=np.array(nums)
print("Part 1 result =",p1:=np.sum(np.abs(nums-int(np.median(nums)))),end='\n\n')



p2=np.inf
idx=0
for i in range(min(nums),mx:=max(nums)+1):
    if not i%100:print('[',int(i*100/mx),'%\t]',p2)    
    res=0
    for num in np.abs(nums-i):
        res+=int(num*(num+1)/2)
    if p2 > res:
        p2=res
        idx=i
    
print("\nPart 2 result =",p2)
print("Done in {:.6f} s".format(time.time()-starttime))
print("\u001b[?25l")

p1v=[]
p2v=[]
for i in range(min(nums),mx:=max(nums)+1):
    res=0
    if not i%100:
        print("Visualization |",end='')
        for c in range(int(i*20/mx)):
            print("\u2588",end='')
        for c in range(19-int(i*20/mx)):
            print(" ",end='')
        print("|\r",end='')
    for num in np.abs(nums-i):
        res+=int(num*(num+1)/2)
    p1v.append(np.sum(np.abs(nums-i)))
    p2v.append(res)
print('')
print("\u001b[?25h")
plt.semilogy(p1v,'k')
plt.semilogy(p2v,'k')
plt.show()
