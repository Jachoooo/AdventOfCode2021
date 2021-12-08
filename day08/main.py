import time

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()



print("\u001b[2J\u001b[0;0H")
inputFile=open(FILENAME,'r')
inp=[x.strip() for x in inputFile.readlines()]



#part 1
res1=0
for msg in inp:
    msg=msg.split('|')[1]
    for num in msg.strip().split(' '):
        if len(num) in [2,3,4,7]:
            res1+=1



#part 2
ret2=0
for msg in inp:
    trueNums=['' for x in range(10)]
    msg=msg.replace(' | ',' ')
    
    for num in msg.split(' '):
        match len(num):
            case 2: trueNums[1]=set(num)
            case 3: trueNums[7]=set(num)
            case 4: trueNums[4]=set(num)
            case 7: trueNums[8]=set(num)

    for num in msg.split(' '):
        if len(num) in [2,3,4,7]:
            continue

        if len(num)==5:
            if len(set(num).intersection(trueNums[1]))==2:
                trueNums[3]=set(num)
                continue
            if len(set(num).intersection(trueNums[4]))==2:
                trueNums[2]=set(num)
            if len(set(num).intersection(trueNums[4]))==3:
                trueNums[5]=set(num)
            continue
        
        if len(num)==6:
            if len(set(num).intersection(trueNums[1]))==2:
                if len(set(num).intersection(trueNums[7]))==3:
                    if len(set(num).intersection(trueNums[4]))==4:
                        trueNums[9]=set(num)
                    else:
                        trueNums[0]=set(num)
            else:
                trueNums[6]=set(num)

    ret2str = ''    
    for j,num in enumerate(msg.split(' ')):
        for i,trueNum in enumerate(trueNums):
            if set(num)==trueNum:
                ret2str+=str(i)
                break
        if j == 9:
            ret2str+=' | '
    
    ret2+=int(ret2str[-4:])
    print(ret2str,'|',ret2)

print("\nPart 1 result =",res1)        
print("Part 2 result =",ret2)
print("Done in {:.6f} s".format(time.time()-starttime))





                

