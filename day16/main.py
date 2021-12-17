import time
from collections import deque
import numpy as np
from numpy import product


FILENAME="test4.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()


print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    msg='F'+file.readline()

print(msg[1:])
print(str(bin(int(msg,base=16)))[6:])
print(10000*10000)
print(product(10000*10000,dtype=np.uint16))
print('-'*50)
msg=str(bin(int(msg,base=16)))[6:]

state='version'
version=''
Id=''
tId=''
i=0
rlen=0
values=deque()
control=0
value=''
res1=0
packetRec=deque()
operation=deque()
mem=deque()
while True:
    if len(msg)<6:
        if operation:
            if state in ['version','ID','value','typeID']:
                state='operation'
        else:
            break

    match state:

        case 'version':
            
            i+=1
            rlen+=3
            version=int(msg[0:3],base=2)
            res1+=version
            msg=msg[3:]

            print(f'\n[{i}] Packet version : \t{version}')
            state='ID'
            
        case 'ID':
            rlen+=3
            Id=int(msg[0:3],base=2)
            msg=msg[3:]
            
            
            print(f'[{i}] Packet ID : \t{Id}')
            if Id==4:
                state='value'
                
            else:
                state='typeID'

        case 'value':
            rlen+=5
            control=msg[0]
            value=value+msg[1:5]
            msg=msg[5:]

            if control=='0':
                Nvalue=int(value,base=2)
                print(f'[{i}] Packet value : \t{Nvalue}')
                state='endValue'
            else:
                state='value'

        case 'endValue':
            values.append(Nvalue)
            value=''
            Nvalue=0
            tempID,cnt=operation.pop()
            cnt+=1
            operation.append((tempID,cnt))
            state='incPackets'

        case 'incPackets':
            for j in range(len(packetRec)):
                tId,L=packetRec.popleft()
                if tId == '0':
                    L-=rlen
                    if L == 0 :
                        state='operation'
                    else:
                        state='version'
                        packetRec.append((tId,L))
                else:
                    L-=1
                    if L == 0 :
                        state='operation'
                    else:
                        state='version'
                        packetRec.append((tId,L))

        case 'operation':
            nums=[]
            tempID,cnt=operation.pop()
            mem.pop()
            if not operation:
                cnt=len(values)
            for j in range(cnt):
                nums.append(values.pop())
            
            match tempID:
                case 0:
                    values.append(sum(nums))
                case 1:
                    values.append(product(nums,dtype=np.uint64))
                case 2:
                    values.append(min(nums))
                case 3:
                    values.append(max(nums))
                case 5:
                    values.append(int(nums[0]<nums[1]))
                case 6:
                    values.append(int(nums[0]>nums[1]))
                case 7:
                    values.append(int(nums[0]==nums[1]))
            
            


            printval=values.pop()
            values.append(printval)
            print(nums)
            print(msg)
            print(f'[{i}] Operation {tempID} = \t{printval}')
            if operation:
                _,bl,rl=mem.pop()
                mem.append((_,bl,rl))
                if _ == '0':
                    print(f'{rl} + {bl} = {rlen}')
                    
                state='version'
                
                if (_ == '0') and rl+bl==rlen:
                    state='operation'
                else:
                    tempID,cnt=operation.pop()
                    cnt+=1
                    operation.append((tempID,cnt))

            else:
                state='break'


        case 'tail':
            msg=msg[4-rlen%4:]
            state='version'

        case 'typeID':
            rlen+=1
            tId=msg[0]
            msg=msg[1:]

            print(f'[{i}] Packet type ID : \t{tId}')
            if tId=='0':
                state='bitLen'
            else:
                state='packetLen'

        case 'bitLen':
            rlen+=15
            bitLen=int(msg[0:15],base=2)
            msg=msg[15:]
            print(f'[{i}] Bit length : \t{bitLen}')
            state='version'
            packetRec.append((tId,bitLen))
            operation.append((Id,0))
            mem.append((tId,bitLen,rlen))

        case 'packetLen':
            rlen+=11
            packetLen=int(msg[0:11],base=2)
            msg=msg[11:]
            print(f'[{i}] Packet length : \t{packetLen}')
            state='version'
            packetRec.append((tId,packetLen))
            operation.append((Id,0))
            mem.append((tId,packetLen,0))

        case _:
            print(f'ERROR! invalid command. "{msg}"')
            break






print(f"\nPart 1 result = {res1}") 

print(f"Part 2 result = {values.pop()}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))


#1760775000
#752770002926
#179254121089391655