import time
FILENAME="input.txt"
DAYS1=80
DAYS2=256
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()



def initdict():
    fishDict={}
    for i in range(9):
        fishDict[i]=0
    return fishDict



def updateDict(fishDict):
    newfish=fishDict[0]
    for i in range(1,9):
        fishDict[i-1]=fishDict[i]
    fishDict[8]=newfish
    fishDict[6]+=newfish
    return fishDict
    


print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')
nums=[int(x) for x in inputFile.readline().strip().split(',')]

if D:print(nums)
fishDict=initdict()
if D:print(fishDict)

for fish in nums:
    fishDict[fish]+=1
if D:print(fishDict)

for i in range(DAYS1):
    fishDict=updateDict(fishDict)
print("Part 1 result =",sum(fishDict.values()))



fishDict=initdict()
for fish in nums:
    fishDict[fish]+=1

for i in range(DAYS2):
    fishDict=updateDict(fishDict)

print("Part 2 result =",sum(fishDict.values()))
print("Done in {:.6f} s".format(time.time()-starttime))