import time
from collections import deque

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.perf_counter()




print("\u001b[2J\u001b[0;0H")
chardict={'>':'<',']':'[','}':'{',')':'('}
valdict={
    ')': 3 ,
    ']': 57 ,
    '}': 1197 ,
    '>': 25137 
}
errors=0
with open(FILENAME,'r') as file:
    for i,line in enumerate(file):
        line = line.strip()
        stack=deque([])
        print(f'[{i}] {line}\t',end='')
        for c in line:
            if stack :

                if c in chardict.values() :
                    stack.append(c)
                    continue
                elif chardict[c]==stack[-1] :
                    stack.pop()
                    continue
                else:
                    print(f'Value error! Expected "{stack[-1]}" Recieved "{c}"',end='')
                    errors+=valdict[c]
                    break
            else :
                stack.append(c)
        print('')

   






print(f"Part 1 result = {errors}")        
print(f"Part 2 result = {0}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
