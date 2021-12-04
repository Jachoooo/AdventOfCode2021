#Advent of Code 2021
#JKL
import time
from copy import deepcopy
FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()

class Board:

    def __init__(self, numBoard,ID):
        self.numBoard = numBoard
        self.ID=ID
    def setCallBoard(self,callDict):
        self.callBoard = deepcopy(self.numBoard)
        for i in range(5):
            for j in range(5):
                self.callBoard[i][j]=callDict[self.callBoard[i][j]]
    def findFirstBingo(self):
        ret=100000000
        for i in range(5):
            ret=min(max(self.callBoard[i][:]),ret)
        for j in range(5):
            ret=min(max([i[j] for i in self.callBoard]),ret)

        return [ret,self.ID]
    def notcalled(self,num):
        ret=0
        ret2=0
        for i in range(5):
            for j in range(5):
                if self.callBoard[i][j]>num:
                    ret+=int(self.numBoard[i][j])
                elif self.callBoard[i][j]==num:
                    ret2=self.numBoard[i][j]

        return ret,int(ret2)
    def printBoard(self,num=99):

        print("board =",self.ID)
        print('+----------------+')
        for i in range(5):
            print("| ",end='')
            for j in range(5):
                if self.callBoard[i][j]<=num:
                    print("\u001b[1m",end='')
                if len(self.numBoard[i][j])==1:
                    print(' '+self.numBoard[i][j],end=' ')
                else:    
                    print(self.numBoard[i][j],end=' ')
                print("\u001b[0m",end='')
            print('|')
        print('+----------------+')
        
        

#Part 1
print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')

numbers=inputFile.readline().strip().split(',')
callDict={}
i=1
for num in numbers:
    callDict[num]=i
    i+=1
if D:print(callDict)  

temp=inputFile.readline()
temp=[]
boards=[]
i=1
for line in inputFile:
    if line != '\n':
        temp.append(
        [st for st in line.strip().split(' ') if st != ''])
    else:
        boards.append(Board(temp,i))
        i+=1
        temp=[]


minScore=1000000000
minID=0
maxScore=0
maxID=0
for i,board in enumerate(boards) :
    board.setCallBoard(callDict) 
    if D:print('\nBoard',i+1,'\n',
    board.numBoard[0],'\t',board.callBoard[0],'\n',
    board.numBoard[1],'\t',board.callBoard[1],'\n',
    board.numBoard[2],'\t',board.callBoard[2],'\n',
    board.numBoard[3],'\t',board.callBoard[3],'\n',
    board.numBoard[4],'\t',board.callBoard[4])
    if D:print('Bingo in',board.findFirstBingo()[0])
    if D:print('Sum =',board.notcalled(board.findFirstBingo()[0])[0])
    tempscore,tempid=board.findFirstBingo()
    if minScore > tempscore:
        minScore=tempscore
        minID=tempid
    if maxScore < tempscore:
        maxScore=tempscore
        maxID=tempid
        
if D:print(minScore,minID)
print('Best',end=' ')
boards[minID-1].printBoard(minScore)
print(
temp1:=boards[minID-1].notcalled(boards[minID-1].findFirstBingo()[0])[0],
'*',
temp2:=boards[minID-1].notcalled(boards[minID-1].findFirstBingo()[0])[1],
'=',
temp1*temp2,'\n')


#Part 2
if D:print(maxScore,maxID)
print('Worst',end=' ')
boards[maxID-1].printBoard(maxScore)
print(
temp1:=boards[maxID-1].notcalled(boards[maxID-1].findFirstBingo()[0])[0],
'*',
temp2:=boards[maxID-1].notcalled(boards[maxID-1].findFirstBingo()[0])[1],
'=',
temp1*temp2,'\n')


print("Done in {:.6f} s".format(time.time()-starttime))
inputFile.close()