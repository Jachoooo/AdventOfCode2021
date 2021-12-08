import time

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()



print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')
inp=[x.strip() for x in inputFile.readlines()]

#part 1
res=0
for msg in inp:
    msg=msg.split('|')[1]
    for num in msg.strip().split(' '):
        if len(num) in [2,3,4,7]:
            res+=1
print(res)
           

