import time
from collections import Counter
import numpy as np
from numpy.core.numerictypes import maximum_sctype
import cProfile
starttime=time.perf_counter()

FILENAME="input.txt"
D=False

instructions=[]
coords=[]
with open(FILENAME,'r') as file:
    for line in file:
        instructions.append(line)

class ID:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

class inst:
    def __init__(self,coords,onoff):
        self.coords=coords
        self.on=onoff


class confirmedArea:
    def __init__(self,coords,intersects,nonintersects):
        self.coords=coords
        self.nonintersects=nonintersects
        self.intersects=intersects

class cube:

    def __init__(self,coords) -> None:
        self.coords=coords
        self.cutouts=[]

    def addCutout(self,cutCoords):
        retcoords=calcIntersect(self.coords,cutCoords)
        if not retcoords:
            return
        for cutout in self.cutouts:
            cutout.addCutout(retcoords)
        self.cutouts.append(cube(retcoords))
    def volume(self):
        return calcArea(self.coords) - sum(cutout.volume() for cutout in self.cutouts)    


def calcArea(retCoords):
    area=1
    for i in range(3):
        area*=retCoords[i][1]+1-retCoords[i][0]
    if area<=0:
        return 0
    return area

def calcIntersect(Coords1,Coords2):
    retCoords=[[0,0],[0,0],[0,0]]
    for i in range(3):
        retCoords[i][0]=max(Coords1[i][0],Coords2[i][0])
        retCoords[i][1]=min(Coords1[i][1],Coords2[i][1])

    area=calcArea(retCoords)
    if area==0:
        return None
    return retCoords



myclass = ID()
myiter = iter(myclass)


with cProfile.Profile() as pr:



    confirmedAreas=[]
    res=0
    for i,instruction in enumerate(instructions):

        #Generate instruction from input
        OnOff=instruction.split(' ')[0]
        coords=instruction.split(' ')[1].strip().split(',')
        coords=[[int(num) for num in coord[2:].split('..')] for coord in coords]
        if OnOff=='on':
            On=True
        else:
            On=False
        
        print(coords)

        for area in confirmedAreas:
            
            area.addCutout(coords)
        if On:
            confirmedAreas.append(cube(coords))
        if i>40:break
        print(sum(area.volume() for area in confirmedAreas))

pr.print_stats() 

print(f"\nResult = {sum(area.volume() for area in confirmedAreas)}")  

print("Done in {:.6f} s".format(time.perf_counter()-starttime))