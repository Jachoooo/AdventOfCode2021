import time
import numpy as np
from PIL import Image
FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()

def bucketfill(num,array,y,x):
    array[y,x]=num
    if x-1 != -1 : 
        if array[y,x-1] == 0 : bucketfill(num,array,y,x-1)
    if x+1 < array.shape[1] : 
        if array[y,x+1] == 0: bucketfill(num,array,y,x+1)
    if y-1 >= 0 : 
        if array[y-1,x] == 0 : bucketfill(num,array,y-1,x)
    if y+1 < array.shape[0] : 
        if array[y+1,x] == 0 : bucketfill(num,array,y+1,x)



print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    arr=np.array([[int(y) for y in x.strip()] for x in file])


#part 1
mins=np.zeros_like(arr)
maxs=np.zeros_like(arr)
for (y,x),elem in np.ndenumerate(arr):
    if elem==9 : 
        maxs[y,x]=-1
        continue
    if x-1 >= 0 : 
        if arr[y,x-1]<=elem : continue
    if x+1 < arr.shape[1] : 
        if arr[y,x+1]<=elem : continue
    if y-1 >= 0 : 
        if arr[y-1,x]<=elem : continue
    if y+1 < arr.shape[0] : 
        if arr[y+1,x]<=elem : continue

    mins[y,x]=1


#part 2
i=1
for (y,x),elem in np.ndenumerate(maxs):
    if elem == -1 : continue
    if elem == 0 :
        bucketfill(i,maxs,y,x)
        i+=1
    
basins=[]
for i in range(1,np.max(maxs)+1):   
    basins.append(np.sum(maxs==i))

basins=np.sort(basins)



print(f"Part 1 result = {np.sum((arr+1)*mins)}")        
print(f"Part 2 result = {basins[-1]*basins[-2]*basins[-3]}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))

img=Image.fromarray((np.ones_like(maxs)*100)+((maxs>0)*150)-mins*250)
img.show()
img=img.convert('RGB')
img.save('GS.png',bitmap_format='png')

im=np.array([mins*100,np.zeros_like(maxs),(maxs>0)*100])
im=np.moveaxis(im,0,2)
print(im.shape)
img=Image.fromarray(im.astype(np.uint8))
img.show()
img=img.convert('RGB')
img.save('RGB.png',bitmap_format='png')