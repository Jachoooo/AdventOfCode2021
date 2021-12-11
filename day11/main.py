import time
import numpy as np
STOP=100
FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()



def printarray(array):
    for y in range(1,11):
        for x in range(1,11):
            if array[y,x]==0 :
                print('\u001b[1m0 \u001b[22m',end='')
            else:
                print(array[y,x],end=' ')
        print('')



print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    array=np.genfromtxt(file,delimiter=1,dtype=np.int16)
array=np.pad(array,1,mode='constant',constant_values=-0xfff)

step=0
flashes=0
tempflashes=0
res1=0

while tempflashes<100 :

    tempflashes=0    
    array=array+1
    flashtable=np.ones_like(array)

    while np.sum(array>=10) != 0 :
        Tflashtable=np.ones_like(array)

        for (y,x),elem in np.ndenumerate(array):
            if elem >= 10 and flashtable[y,x]==1:
                Tflashtable[y,x]=0

        for (y,x),F in np.ndenumerate(Tflashtable):
            if not F and flashtable[y,x]:
                array[y-1:y+2,x-1:x+2]+=1

        flashtable &= Tflashtable
        array *= flashtable
                
    flashes+=np.sum(flashtable==0)
    tempflashes=np.sum(flashtable==0)

    print("\u001b[0;0H")
    print(f'[Step = {step+1:<7} Flashes={flashes:<7}]')

    step+=1
    
    if step == 100: 
        res1= flashes
        res1arr=np.copy(array)

printarray(res1arr)
print(f"\nPart 1 result = {res1}")        
print(f"Part 2 result = {step}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
