import time
import numpy as np
from numpy import character, product
starttime=time.perf_counter()

FILENAME="input.txt"
D=False

chardict={'#':1,'.':0}
print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    code=file.readline()
    _=file.readline()
    mat=np.array([line.strip() for line in file])


def prettyprint(mat):
    for y in range(mat.shape[0]):
            print('|',end='')
            for x in range(mat.shape[1]):
                if mat[y,x]==1:
                    print('# ',end='')
                else:
                    print('  ',end='')
            print('|')
    


def expand(mat,pad):
    global code
    mat=np.pad(mat,2,'constant', constant_values=pad)
    temp=np.copy(mat)
    

    for y in range(mat.shape[0]-2):            
        for x in range(mat.shape[1]-2):
            if D:print(y,x)
            
            num=str(np.ravel(temp[y:y+3,x:x+3])).replace(' ','')[1:-1]
            if D:print(num)
            num=int(num,base=2)
            if D:print(code[num])
            if code[num]=='#':
                mat[y+1,x+1]=1
            else:
                mat[y+1,x+1]=0
    
    mat=mat[1:-1,1:-1]
    
    
    return mat,abs(pad-1)




image=np.zeros((mat.shape[0],mat.shape[0]),dtype=np.int0)

for y,elem in np.ndenumerate(mat):
    for x,c in enumerate(elem):
        if c == '#':
            image[y,x]=1
        else:
            image[y,x]=0
  


#image=np.pad(image,1,'constant', constant_values=0)    
pad=0
for i in range(50):
    print(2*i,'%')
    
    image,pad=expand(image,pad)


print(f"\nResult = {np.sum(image)}") 

print("Done in {:.6f} s".format(time.perf_counter()-starttime))

#5150
#5461 OK
#5617
#5696

#18226