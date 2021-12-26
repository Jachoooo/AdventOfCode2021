import time
import numpy as np



FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()


print("\u001b[2J\u001b[0;0H")

with open(FILENAME,'r') as file:
    mat=np.genfromtxt(file,delimiter=1,dtype=str)


def printmat(mat):
    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            print(mat[y,x],end=' ')
        print('')

#if D:printmat(mat)

def advance(mat):
    change=False
    ret=np.copy(mat)
    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            if mat[y,x]=='>':
                if mat[y,(x+1)%mat.shape[1]]=='.':
                    ret[y,x]='.'
                    ret[y,(x+1)%mat.shape[1]]='>'
                    change=True

    mat=np.copy(ret)
    
    for x in range(mat.shape[1]):
        for y in range(mat.shape[0]):
            if mat[y,x]=='v':
                if mat[(y+1)%mat.shape[0],x]=='.':
                    ret[y,x]='.'
                    ret[(y+1)%mat.shape[0],x]='v'
                    change=True
    return ret,change


i=0
change=True
while change:  
    i+=1          
    mat,change=advance(mat)
    print("\u001b[0;0H")
    print(f'Step {i}')
    print('')
    if D:printmat(mat)
    

print(f"\nPart 1 result = {i}") 
print("Done in {:.6f} s".format(time.perf_counter()-starttime))