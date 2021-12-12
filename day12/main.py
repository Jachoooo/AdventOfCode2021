import time

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()

class node:
    def __init__(self,name) -> None:
        self.name=name
        self.connected=set()
    def add_ngbr(self,name):
        self.connected.add(name)
    

def search1(visited):
    global nodes
    global paths
    global D
    vislist=visited.split(',')
    curNode=vislist[-1]
    if D:print('[1]Searching in ',nodes[curNode].connected)
    for ngbr in nodes[curNode].connected:
        if ngbr=='end':
            if D:print(visited+','+'end')
            paths.add(visited+','+'end')
            continue
        if ngbr.isupper():
            search1(visited+','+ngbr)    
        if (not ngbr.isupper()) and not(ngbr in vislist):
            search1(visited+','+ngbr)


def search2(visited,sm_cave):
    global nodes
    global paths2
    global D
    vislist=visited.split(',')
    curNode=vislist[-1]
    if sm_cave in vislist:
        vislist.remove(sm_cave)
    if D:print('[2]Searching in ',nodes[curNode].connected)
    for ngbr in nodes[curNode].connected:
        if ngbr=='end':
            if D:print(visited+','+'end')
            paths2.add(visited+','+'end')
            continue
        if ngbr.isupper():
            search2(visited+','+ngbr,sm_cave)    
        if (not ngbr.isupper()) and not(ngbr in vislist):
            search2(visited+','+ngbr,sm_cave)


paths=set()
paths2=set()
nodes={}
print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    for line in file:
        node1,node2=line.strip().split('-')
        n1=node(node1)
        n2=node(node2)

        if node1 in nodes.keys():
            nodes[node1].add_ngbr(node2)
        else:
            nodes[node1]=n1
            nodes[node1].add_ngbr(node2)

        if node2 in nodes.keys():
            nodes[node2].add_ngbr(node1)
        else:
            nodes[node2]=n2
            nodes[node2].add_ngbr(node1)



search1('start')
print('[Part 1] Done!')
i=0
for elem in nodes.values():
    if not(elem.name.isupper() or (elem.name in ['start','end'])):i+=1
j=0
for elem in nodes.values():
    if elem.name.isupper() or (elem.name in ['start','end']):
        continue
    else:
        search2('start',elem.name)
        j+=1
        print('[Part 2]',int(j*100/i),'%')




print(f"Part 1 result = {len(paths)}")     
print(f"Part 2 result = {len(paths2)}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
