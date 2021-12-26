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
    
    for i,line in enumerate(instructions):
        
        inst=line[:3]
        nums=line[4:]
        #print(f'[{i}] | {inst},{nums}    \t{registers}                          ')

        
        
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


for block in blocks:
    print("\u001b[0;0H")
    for line in block:
        print(line,'     ')
    

for i,block in enumerate(blocks):
    print(str(i).rjust(10, ' '),end=',')
print('')
for block in blocks:
    print(block[3][:].rjust(10, ' '),end=',')
print('')
for block in blocks:
    print(block[4][:].rjust(10, ' '),end=',')
print('')
for block in blocks:
    print(block[14][:].rjust(10, ' '),end=',')
print('')

pairs=[(0,13),
    (1,12),
    (2,3),
    (4,5),
    (6,7),
    (9,10),
    (8,11)]

pairdict={}

for pair in pairs:
    for w2 in range(1,10):  
        for w in range(1,10):   
            registers={'w':w,
                'x':0,
                'y':0,
                'z':0}
            
            registers=execfile(registers,blocks[pair[0]])
            registers['w']=w2
            if execfile(registers,blocks[pair[1]])['z']==0:
                pairdict[str(pair)]=(w,w2)

print(pairdict)
temp=['_','_','_','_','_','_','_','_','_','_','_','_','_','_'] 

for pair in pairs:
    temp[pair[0]]=pairdict[str(pair)][0]
    temp[pair[1]]=pairdict[str(pair)][1]

res1=''
for c in temp:
    res1+=str(c)




for pair in pairs:
    for w2 in range(1,10).__reversed__():  
        for w in range(1,10).__reversed__():   
            registers={'w':w,
                'x':0,
                'y':0,
                'z':0}
            
            registers=execfile(registers,blocks[pair[0]])
            registers['w']=w2
            if execfile(registers,blocks[pair[1]])['z']==0:
                pairdict[str(pair)]=(w,w2)

print(pairdict)
temp=['_','_','_','_','_','_','_','_','_','_','_','_','_','_'] 

for pair in pairs:
    temp[pair[0]]=pairdict[str(pair)][0]
    temp[pair[1]]=pairdict[str(pair)][1]

res2=''
for c in temp:
    res2+=str(c)

print(f"\nPart 1 result = {res1}")     
print(f"Part 2 result = {res2}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
