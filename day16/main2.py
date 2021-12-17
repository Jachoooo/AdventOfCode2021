import time
import numpy as np
from numpy import product


FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()


print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    m='F'+file.readline()

print(m[1:])
print(str(bin(int(m,base=16)))[6:])
print('-'*50)
m=str(bin(int(m,base=16)))[6:]

ret1=0
def readpacket(msg):
    global ret1
    print(msg[0:3],msg[3:6],msg[6:])
    version=int(msg[0:3],base=2)
    ret1+=version
    Id=int(msg[3:6],base=2)
    msg=msg[6:]
    bitlen=6
    if Id == 4:
        value=''
        while True:
            control=msg[0]
            value=value+msg[1:5]
            msg=msg[5:]
            bitlen+=5
            if control=='0':
                print('value =',int(value,base=2))
                return int(value,base=2),bitlen,msg   
    
    typ=int(msg[0],base=2)
    msg=msg[1:]
    bitlen+=1
    if typ == 0 :
        length=int(msg[0:15],base=2)
        msg=msg[15:]
        bitlen+=15
        stop=0
        ret=[]
        while stop<length:
            t1,t2,msg=readpacket(msg)
            ret.append(t1)
            stop+=t2
            bitlen+=t2
    else:
        length=int(msg[0:11],base=2)
        msg=msg[11:]
        bitlen+=11
        ret=[]
        for i in range(length):
            t1,t2,msg=readpacket(msg)
            ret.append(t1)
            bitlen+=t2

    match Id:
            case 0:
                return sum(ret),bitlen,msg
            case 1:
                return product(ret,dtype=np.int64),bitlen,msg
            case 2:
                return min(ret),bitlen,msg
            case 3:
                return max(ret),bitlen,msg
            case 5:
                return int(ret[0]>ret[1]),bitlen,msg
            case 6:
                return int(ret[0]<ret[1]),bitlen,msg
            case 7:
                return int(ret[0]==ret[1]),bitlen,msg

    raise Exception

ret2,c1,c2=readpacket(m)
if c1 != len(m):print("WRONG LENGTH",abs(c1-len(m)))
if len(c2)!=0:print("POSSIBLE LEFTOVER",c2)

print(f"\nPart 1 result = {ret1}") 

print(f"Part 2 result = {ret2}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))

#1760775000

#180616437720 OK

#752770002926
#179254121089391655