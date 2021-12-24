import time
from copy import copy
from math import floor

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()


registers={'w':0,
    'x':0,
    'y':0,
    'z':0}
num='13579246899990'
num='__________0190'
iternum=iter(num)
blocks=[]
instructions=[]

with open(FILENAME,'r') as file:
    for line in file:
        
        if line[0:3]=='inp':
            if instructions:
                blocks.append(instructions)
            instructions=[]
        else:
            instructions.append(line.strip())
    blocks.append(instructions)

print("\u001b[2J\u001b[0;0H")

def execfile(registers,instructions):
    print("\u001b[0;0H")
    for i,line in enumerate(instructions):
        
        inst=line[:3]
        nums=line[4:]
        print(f'[{i}] | {inst},{nums}    \t{registers}                          ')

        
        
        global iternum
        if inst=='inp':
            break
            registers[nums]=int(next(iternum))
            print('-'*60,registers[nums])
            continue

        a,b=nums.split(' ')

        if b.replace('-','').isnumeric():
            b=int(b)
        else:
            b=registers[b]

        match inst:    
            case 'add':
                registers[a]=registers[a]+b    

            case 'mul':
                registers[a]=registers[a]*b 

            case 'div':
                if b==0: raise ValueError
                registers[a]=floor(registers[a]/b)


            case 'mod':
                if registers[a]<0 or b<=0: raise ValueError
                registers[a]=registers[a]%b

            case 'eql':
                if registers[a]==b:
                    registers[a]=1
                else:
                    registers[a]=0



            case _:
                raise ValueError
    return registers


blocks.reverse()




for w in range(0,10):
    for z in range(10000):   
        registers={'w':w,
            'x':0,
            'y':0,
            'z':z}
        
        if(execfile(registers,blocks[0])['z']==594):
            print(f'w={w}\tz={z}')
'43210'
'99920'    
print(f"\nPart 1 result = {registers['z']}")     
print(f"Part 2 result = {0}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
