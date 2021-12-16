import time
import numpy as np
import cProfile
import heapq

FILENAME="test.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()


print("\u001b[2J\u001b[0;0H")
with open(FILENAME,'r') as file:
    maze=np.genfromtxt(file,delimiter=1,dtype=np.int16)


stop=False
curpos=(0,0)
end=(maze.shape[1]-1,maze.shape[0]-1)
updated=np.zeros_like(maze)
updated[0,0]=1
OGmaze=np.copy(maze)
maze2=np.copy(maze)

def search(y,x,updated,maze):
    global OGmaze
    

    #time.sleep(1)
    if x == maze.shape[1]-1 and y==maze.shape[0]-1:
        
        return 1

    if y != maze.shape[1]-1 and x != maze.shape[0]-1:

        if maze[y+1,x] < maze[y,x+1]:
            
            if updated[y+1,x]==0:
                updated[y+1,x]=1
                maze[y+1,x]+=maze[y,x]
                search(y+1,x,updated,maze)
            elif OGmaze[y+1,x]+maze[y,x]<maze[y+1,x]:
                maze[y+1,x]=OGmaze[y+1,x]+maze[y,x]
                search(y+1,x,updated,maze)

            
            if updated[y,x+1]==0:
                updated[y,x+1]=1
                maze[y,x+1]+=maze[y,x]
                search(y,x+1,updated,maze)
            elif OGmaze[y,x+1]+maze[y,x]<maze[y,x+1]:
                maze[y,x+1]=OGmaze[y,x+1]+maze[y,x]
                search(y,x+1,updated,maze)
        else:
            
            
            if updated[y,x+1]==0:
                updated[y,x+1]=1
                maze[y,x+1]+=maze[y,x]
                search(y,x+1,updated,maze)
            elif OGmaze[y,x+1]+maze[y,x]<maze[y,x+1]:
                maze[y,x+1]=OGmaze[y,x+1]+maze[y,x]
                search(y,x+1,updated,maze)
            
            
            if updated[y+1,x]==0:
                updated[y+1,x]=1
                maze[y+1,x]+=maze[y,x]
                search(y+1,x,updated,maze)
            elif OGmaze[y+1,x]+maze[y,x]<maze[y+1,x]:
                maze[y+1,x]=OGmaze[y+1,x]+maze[y,x]
                search(y+1,x,updated,maze)
    else:
        if x != maze.shape[0]-1:
                if updated[y,x+1]==0:
                    updated[y,x+1]=1
                    maze[y,x+1]+=maze[y,x]
                    search(y,x+1,updated,maze)
                elif OGmaze[y,x+1]+maze[y,x]<maze[y,x+1]:
                    maze[y,x+1]=OGmaze[y,x+1]+maze[y,x]
                    search(y,x+1,updated,maze)
            
        if y != maze.shape[1]-1:
            if updated[y+1,x]==0:
                updated[y+1,x]=1
                maze[y+1,x]+=maze[y,x]
                search(y+1,x,updated,maze)
            elif OGmaze[y+1,x]+maze[y,x]<maze[y+1,x]:
                maze[y+1,x]=OGmaze[y+1,x]+maze[y,x]
                search(y+1,x,updated,maze)

search(0,0,updated,maze)
print(f"Part 1 result = {maze[-1,-1]-1}") 
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
starttime=time.perf_counter()

maze21=np.ones_like(maze2)+((maze2<9)*maze2)
maze22=np.ones_like(maze21)+((maze21<9)*maze21)
maze23=np.ones_like(maze22)+((maze22<9)*maze22)
maze24=np.ones_like(maze23)+((maze23<9)*maze23)
maze25=np.ones_like(maze24)+((maze24<9)*maze24)
maze26=np.ones_like(maze25)+((maze25<9)*maze25)
maze27=np.ones_like(maze26)+((maze26<9)*maze26)
maze28=np.ones_like(maze27)+((maze27<9)*maze27)

maze2=np.block([
    [maze2,maze21,maze22,maze23,maze24],
    [maze21,maze22,maze23,maze24,maze25],
    [maze22,maze23,maze24,maze25,maze26],
    [maze23,maze24,maze25,maze26,maze27],
    [maze24,maze25,maze26,maze27,maze28]
])



maze2=np.pad(maze2,1,'constant',constant_values=10000)


def djikstra(maze):
    

    # These are all the nodes which have not been visited yet
    unvisited = {(index[0]+1,index[1]+1): 10000 for index,_ in np.ndenumerate(maze2[1:-1,1:-1])}
    # It will store the shortest distance from one node to another
    visited = {}
    h=[]
    heapq.heappush
    current = (1,1)
    # It will store the predecessors of the nodes
    currentDistance = 0
    unvisited[current] = currentDistance
    # Running the loop while all the nodes have been visited
    while True:
        # iterating through all the unvisited node
        for neighbour, distance in zip([
            (current[0],current[1]+1),
            (current[0],current[1]-1),
            (current[0]+1,current[1]),
            (current[0]-1,current[1])],
            [maze2[(current[0],current[1]+1)],
            maze2[(current[0],current[1]-1)],
            maze2[(current[0]+1,current[1])],
            maze2[(current[0]-1,current[1])]
            ]):
            # Iterating through the connected nodes of current_node (for 
            # example, a is connected with b and c having values 10 and 3
            # respectively) and the weight of the edges
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
                heapq.heappush(h,(newDistance,neighbour))
        # Till now the shortest distance between the source node and target node 
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        if current==(maze2.shape[0]-2,maze2.shape[1]-2):return visited
        del unvisited[current]
        if not unvisited: break
        
        currentDistance,current =heapq.heappop(h)
        #current, currentDistance = sorted(unvisited.items(), key = lambda x: x[1])[0]

    return visited
    
ret2=djikstra(maze2)[(maze2.shape[0]-2,maze2.shape[1]-2)]

    
print(f"Part 2 result = {ret2}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
#2838
