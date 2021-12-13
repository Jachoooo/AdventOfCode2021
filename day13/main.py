import time
import numpy as np

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()



x=[]
y=[]
foldax=[]
foldval=[]
print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    for line in file:
        if line[0].isnumeric():
            xt,yt=[int(i) for i in line.split(',')]
            x.append(xt)
            y.append(yt)
        elif line == '\n':
            continue
        else:
            foldax.append(line.split(' ')[2].split('=')[0])
            foldval.append(int(line.split(' ')[2].split('=')[1]))



def printmat(x,y):
    maxx=max(x)
    maxy=max(y)
    mat=np.zeros((maxy+1,maxx+1),dtype=np.int8)
    for temp in zip(y,x):
        mat[temp]=1

    
    if maxx <100 and maxy<100:
        for yi in range(mat.shape[0]):
            for xi in range(mat.shape[1]):
                if mat[yi,xi]==1:
                    print('#',end='')
                else:
                    print(' ',end='')
            print('')

    print('Sum after fold =',np.sum(mat))



for i,val in enumerate(foldval):
    ax=foldax[i]
    maxx=max(x)
    maxy=max(y)

    match ax:
        case 'x':
            for j,elem in enumerate(x):
                if elem>val:
                    x[j]=(2*val)-elem
        case 'y':
            for j,elem in enumerate(y):
                if elem>val:
                    y[j]=(2*val)-elem
    
    printmat(x,y)
    print(f'fold {i+1} done.')



print(f"Part 1 result = {731}")     
print(f"Part 2 result = ZKAUCFUC")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
