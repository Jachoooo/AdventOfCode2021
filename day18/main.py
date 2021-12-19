import time
from math import floor,ceil



FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()

class ShellNum:

    
    def __init__(self,num,depth) -> None:

        self.depth=depth
        num=num[1:-1]
        temp=0
        for i,c in enumerate(num):
            if c=='[':
                temp+=1
            if c==']':
                temp-=1
            if c==','and temp==0:
                #print(num[0:i],num[i+1:])
                if num[0:i].isnumeric():
                    self.left=int(num[0:i])
                else:
                    self.left=ShellNum(num[0:i],depth+1)

                if num[i+1:].isnumeric():
                    self.right=int(num[i+1:])    
                else:
                    self.right=ShellNum(num[i+1:],depth+1)

                break
                
    def __str__(self) -> str:
        return '['+str(self.left)+','+str(self.right)+']'

    def isExplode(self) -> bool:

        l=False
        r=False
        
        if self.depth>4:
            return True
        
        if type(self.left) != int:
            l=self.left.isExplode()
                
        if type(self.right) != int:
            r=self.right.isExplode()
        
        return l or r
    
    def isSplit(self) -> bool:
        
        l=False
        r=False

        if type(self.left) != int:
            l=self.left.isSplit()
        elif self.left>9:
            l=True
                        
        if type(self.right) != int:
            r=self.right.isSplit()
        elif self.right>9:
            r=True
        
        return r or l
        
    def isNotValid(self) -> bool:
        return self.isExplode() or self.isSplit()         
    
    def ReduceNum(self):
        while self.isNotValid():

            if self.isExplode():
                continue

            if self.isSplit():
                continue
            


        pass       

    def Explode(self):
        
        strg=self.__str__()
        temp=0
        l=0
        r=0
        for i,c in enumerate(strg):
            if c=='[':
                temp+=1
                l=i
            if c==']':
                if temp>4:
                    r=i
                     
                    lnum=int(strg[l+1:r].split(',')[0])
                    rnum=int(strg[l+1:r].split(',')[1])
                    lstr=strg[:l]
                    rstr=strg[r+1:]
                    
                    temp=''
                    for i,c in enumerate(lstr[::-1]):
                        if c.isnumeric():
                            temp=c+temp
                            idx=i
                        else:
                            if temp:
                                finalnum=str(int(temp)+lnum)
                                lstr=lstr[:len(lstr)-idx-1]+finalnum+lstr[len(lstr)-idx-1+len(temp):]
                                break

                    temp=''
                    for i,c in enumerate(rstr):
                        if c.isnumeric():
                            temp=temp+c
                            idx=i
                        else:
                            if temp:
                                finalnum=str(int(temp)+rnum)
                                
                                rstr=rstr[:idx-len(temp)+1]+finalnum+rstr[idx+1:]
                                break
                    
                    

                    break 
                else :
                    temp-=1
        ret=lstr+'0'+rstr
            
        self.__init__(ret,1)    
        
    def Split(self):
        strg=self.__str__()
        temp=''
        r=0
        
        for i,c in enumerate(strg):
            if c.isnumeric():
                r=i
                temp=temp+c
            else:
                if temp:
                    if int(temp)>9:
                        num=int(temp)
                        ln=floor(num/2)
                        rn=ceil(num/2)
                        mid='['+str(ln)+','+str(rn)+']'
                        ret=strg[:r-len(temp)+1]+mid+strg[r+1:]
                        
                        break
                    
                
                temp=''
                r=0
        self.__init__(ret,1)   
        
    def maginitude(self) -> int:
        
        if type(self.left) != int:
            l=self.left.maginitude()
        else:
            l=self.left
                        
        if type(self.right) != int:
            r=self.right.maginitude()
        else:
            r=self.right
        
        return (l*3)+(r*2)

def validateNum(MainNum):
    while MainNum.isNotValid():

            if MainNum.isExplode():
                MainNum.Explode()
                if D:print('[X] ',MainNum)
                
                continue

            if MainNum.isSplit():
                MainNum.Split()
                if D:print('[S] ',MainNum)
                       
                continue



print("\u001b[2J\u001b[0;0H")


with open(FILENAME,'r') as file:

    num=file.readline().strip()
    MainNum=ShellNum(num,1)
    if D:print('[M] ',MainNum)
    validateNum(MainNum)
    if D:print(MainNum)
    for line in file:
        MainNum=ShellNum('['+str(MainNum)+','+line.strip()+']',1)
        if D:print('[N] ',MainNum)
        validateNum(MainNum)
        if D:print('[V] ',MainNum)


with open(FILENAME,'r') as file:
    nums=[line.strip() for line in file]


res2=0

for i,num1 in enumerate(nums):
    for num2 in nums[i:]:
        temp=ShellNum('['+num1+','+num2+']',1)
        validateNum(temp)
        res2=max(res2,temp.maginitude())

    if D:print(100*i/len(nums),'%')
    

print(f"\nPart 1 result = {MainNum.maginitude()}") 
print(f"Part 2 result = {res2}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))