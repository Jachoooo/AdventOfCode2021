import time
import numpy as np
from collections import Counter

from numpy.core.fromnumeric import sort



FILENAME="input.txt"
if FILENAME[0:4]=="test":
    D=True
else:
    D=False

starttime=time.perf_counter()


class scanner:
    def __init__(self,name,coords) -> None:
        self.name=name
        self.id=name.split(' ')[2]
        self.coords=coords
        self.xyz=[[int(coord) for coord in elem.split(',')] for elem in coords]
        if D:print('x=',self.xyz[0][0])
        if D:print('y=',self.xyz[0][1])
        if D:print('z=',self.xyz[0][2])
        self.xyz=np.array(self.xyz)
        if D:print('\nx=',self.xyz[0][0])
        if D:print('y=',self.xyz[0][1])
        if D:print('z=',self.xyz[0][2])
        self.distances=[]
        for i in range(self.xyz.shape[0]):
            for j in range(i+1,self.xyz.shape[0]):
                self.distances.append(np.sum(np.square(np.abs(self.xyz[i]-self.xyz[j]))))
               
    def getCoords(self,transform):

        match transform:
            case 1:
                tmat=np.array([
                    [1,0,0],
                    [0,1,0],
                    [0,0,1]
                ])
            case 2:
                tmat=np.array([
                    [1,0,0],
                    [0,0,-1],
                    [0,1,0]
                ])
            case 3:
                tmat=np.array([
                    [1,0,0],
                    [0,-1,0],
                    [0,0,-1]
                ])
            case 4:
                tmat=np.array([
                    [1,0,0],
                    [0,0,1],
                    [0,-1,0]
                ])
            ############################################
            case 5:
                tmat=np.array([
                    [0,-1,0],
                    [1,0,0],
                    [0,0,1]
                ])
            case 6:
                tmat=np.array([
                    [0,0,1],
                    [1,0,0],
                    [0,1,0]
                ])
            case 7:
                tmat=np.array([
                    [0,1,0],
                    [1,0,0],
                    [0,0,-1]
                ])
            case 8:
                tmat=np.array([
                    [0,0,-1],
                    [1,0,0],
                    [0,-1,0]
                ])
            ##################################################
            case 9:
                tmat=np.array([
                    [-1,0,0],
                    [0,-1,0],
                    [0,0,1]
                ])
            case 10:
                tmat=np.array([
                    [-1,0,0],
                    [0,0,-1],
                    [0,-1,0]
                ])
            case 11:
                tmat=np.array([
                    [-1,0,0],
                    [0,1,0],
                    [0,0,-1]
                ])
            case 12:
                tmat=np.array([
                    [-1,0,0],
                    [0,0,1],
                    [0,1,0]
                ])
            ##################################################
            case 13:
                tmat=np.array([
                    [0,1,0],
                    [-1,0,0],
                    [0,0,1]
                ])
            case 14:
                tmat=np.array([
                    [0,0,1],
                    [-1,0,0],
                    [0,-1,0]
                ])
            case 15:
                tmat=np.array([
                    [0,-1,0],
                    [-1,0,0],
                    [0,0,-1]
                ])          
            case 16:
                tmat=np.array([
                    [0,0,-1],
                    [-1,0,0],
                    [0,1,0]
                ])
            ######################################################    
            case 17:
                tmat=np.array([
                    [0,0,-1],
                    [0,1,0],
                    [1,0,0]
                ])
            case 18:
                tmat=np.array([
                    [0,1,0],
                    [0,0,1],
                    [1,0,0]
                ])
            case 19:
                tmat=np.array([
                    [0,0,1],
                    [0,-1,0],
                    [1,0,0]
                ])
            case 20:
                tmat=np.array([
                    [0,-1,0],
                    [0,0,-1],
                    [1,0,0]
                ])
            ######################################################
            case 21:
                tmat=np.array([
                    [0,0,-1],
                    [0,-1,0],
                    [-1,0,0]
                ])
            case 22:
                tmat=np.array([
                    [0,-1,0],
                    [0,0,1],
                    [-1,0,0]
                ])
            case 23:
                tmat=np.array([
                    [0,0,1],
                    [0,1,0],
                    [-1,0,0]
                ])
            case 24:
                tmat=np.array([
                    [0,1,0],
                    [0,0,-1],
                    [-1,0,0]
                ])

        
        return np.array([tmat.dot(coord) for coord in self.xyz])
        


print("\u001b[2J\u001b[0;0H")
print(np.square(np.array([1,2,3,4,5])))


with open(FILENAME,'r') as file:
    scanners=[]
    temp=[]
    for line in file:
        if line=='\n':
            
            scanners.append(scanner(name,temp))
            temp=[]
        elif line[0:3]=='---':
            name=line.strip()
        else:
            temp.append(line.strip())
        

        
        
MINMATCH=12
possiblepairs=[]
for i in range(len(scanners)):
    for j in range(i+1,len(scanners)):
        
        c1=Counter(scanners[i].distances)
        c2=Counter(scanners[j].distances)
        if len(list((c1&c2).elements()))>=MINMATCH*(MINMATCH-1)/2:
            print(f'[{i},{j}] = ',len(list((c1&c2).elements())))
            possiblepairs.append((i,j))


mat1=scanners[0].getCoords(1)
offset0=mat1[0]-mat1[0]
confirmed=dict()
confirmed[0]=(1,offset0)
progress=len(possiblepairs)

confirmed={0: (1, np.array([0, 0, 0])), 
2: (4, np.array([  62,   83, 1085])), 3: (19, np.array([  85, 1284,   -8])), 
22: (10, np.array([-1120,    73,   -57])), 32: (13, np.array([   68,    72, -1227])), 
4: (15, np.array([1283,   26, 1043])), 13: (24, np.array([  -11, -1141,  1124])), 
29: (3, np.array([ 1299, -1266,  1187])), 8: (6, np.array([  140, -1224,  2275])), 
9: (9, np.array([-1097, -1125,  2394])), 18: (11, np.array([    8, -1116,  3605])), 
11: (8, np.array([-1116,    54,  2257])), 1: (16, np.array([-2340,    45,  2245])), 
7: (5, np.array([-2405,  1208, 2353])), 17: (7, np.array([-2245, -1238,  2243])), 
33: (2, np.array([-2373,   -94,  1157])), 34: (13, np.array([-2373,   -96,  3436])), 
19: (20, np.array([-2303,  1234,  1201])), 6: (17, np.array([-2268,  2335,  1210])), 
30: (16, np.array([-1163, -1113,  1084])), 10: (14, np.array([-1132,  1145,  1047])), 
16: (2, np.array([  -13, -2341,  1101])), 24: (4, np.array([-2277, -1225,  1187])), 
35: (4, np.array([ 1198, -1288,  3594])), 28: (1, np.array([-1164,    75, -1298])), 
31: (11, np.array([-2363,   -14,   -95])), 15: (22, np.array([-3448,   -14,   -69])), 
12: (3, np.array([-3514,   -71, -1303])), 25: (9, np.array([-2352,   -32, -1202])), 
20: (12, np.array([-3437,  1132,   -84])), 23: (13, np.array([-4639,   -75,   -58])), 
26: (6, np.array([-4827,  1225,   -61])), 5: (18, np.array([-4699,  2391,  -178])), 
14: (21, np.array([-5870,  1170,    -9])), 27: (17, np.array([-1065,   -43, -2540])),
21: (23, np.array([ 1285, -1180,  2362]))}



while possiblepairs:
    print(possiblepairs)
    print(len(confirmed.keys()),' | ',len(scanners),end=' | ')
    print(confirmed)
    if len(confirmed.keys())==len(scanners):
        break

    print('___________________________\n',progress-len(possiblepairs),'/',progress,'\n___________________________\n')
    A=-1
    B=-1
    for S1,S2 in possiblepairs:
        if S1 in confirmed.keys() and not (S2 in confirmed.keys()):
            A=S1
            B=S2
            break
        if S2 in confirmed.keys() and not (S1 in confirmed.keys()):
            A=S2
            B=S1
            break
        else:
            possiblepairs=possiblepairs[1:]


    
    


    try:
        possiblepairs.remove((A,B))
    except:
        pass
    try:
        possiblepairs.remove((B,A))
    except:
        pass
    if A==B:
        continue
    if A==-1 or B==-1:
        continue

    startrot,startoffset=confirmed[A]
    print(f'Searching pair {A},{B}')
    mat1=scanners[A].getCoords(startrot)+startoffset
    found=False
    for Bor in range(1,25):
        if found: break
        print(int(Bor*100/24),'%')
        mat2=scanners[B].getCoords(Bor)
        offsets=[]
        for i in range(MINMATCH-1,mat1.shape[0]):
            for j in range(MINMATCH-1,mat2.shape[0]):
                offsets.append(mat1[i]-mat2[j])
        for offset in offsets:
            matches=0
            c1=Counter([str(coord) for coord in mat1])
            c2=Counter([str(coord+offset) for coord in mat2])
            if (matches:=len(list((c1&c2).elements())))>=MINMATCH:
                print(f'Match for scanner {A} and {B}\nOrientatios = {1}, {Bor}\n2nd scanner offset = {offset}\nFound {matches} Matches!')
                found=True
                confirmed[B]=(Bor,offset)
                
                break
            if matches>1:
                print(f'[{A}]Offset = {offset} | {matches}')
        
        
        

beacons=[]        
for scanner in scanners:
    try:
        rotation,offset=confirmed[int(scanner.id)]   
    except:
        raise Exception

    for beacon in scanner.getCoords(rotation)+offset:
        beacons.append(str(beacon))

res1=len(Counter(beacons))


maxdist=0
for scanner1 in scanners:
    for scanner2 in scanners:
    
        maxdist=max(maxdist,np.sum(np.abs(confirmed[int(scanner1.id)][1]-confirmed[int(scanner2.id)][1])))   
    

              
        
    



print(f"\nPart 1 result = {res1}") 

print(f"Part 2 result = {maxdist}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))