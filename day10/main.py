import time
from collections import deque
from math import floor

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
scoredict={
    '(': 1 ,
    '[': 2 ,
    '{': 3 ,
    '<': 4 
}
errors=0
res2=[]
with open(FILENAME,'r') as file:
    for i,line in enumerate(file):
        err=False
        line = line.strip()
        stack=deque([])
        print(f'[{i}] ',end='')
        for c in line:
            if not stack : 
                stack.append(c)
                continue
                
            if c in chardict.values() :
                stack.append(c)

            elif chardict[c]==stack[-1] :
                stack.pop()

            else:
                err=True
                break
        
        if err :
            print(f'Value error! Expected "{stack[-1]}" Recieved "{c}"')
            errors+=valdict[c]        
        else :
            stack.reverse()   
            score=0 
            for elem in stack :
                score*=5
                score+=scoredict[elem]
            print(f'Autocomplete score = {score}')
            res2.append(score)


   

res2.sort()

print(f"\nPart 1 result = {errors}")        
print(f"Part 2 result = {res2[floor(len(res2)/2)]}")
print("Done in {:.6f} s".format(time.perf_counter()-starttime))
