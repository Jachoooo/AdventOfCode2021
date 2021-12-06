import time
FILENAME="test.txt"

if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()

def initdict():
    fishDict={}
    for i in range(8):
        fishDict[i]=0
    return fishDict
    


print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')
nums=[int(x) for x in inputFile.readline().strip().split(',')]

if D:print(nums)
if D:print(initdict())