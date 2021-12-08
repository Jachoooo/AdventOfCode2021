import time

FILENAME="input.txt"
if FILENAME=="test.txt":
    D=True 
else:
    D=False
starttime=time.time()


def printmsg(OGmsg,NEWmsg,Nums):
    SPC=29
    print("\u001b[H")
    print('[',OGmsg,end='')
    for i in range(35-len(OGmsg.split('|')[1])):
        print(' ',end='')
    print(']\n[',"                                               ",
          NEWmsg,
          "                             ]")


    nm=NEWmsg.split('|')[1].strip()
    
    chardict={}
    chardict['E']=[x for x in Nums[8].difference(Nums[9])][0]
    chardict['G']=[x for x in Nums[8].difference(Nums[0])][0]
    chardict['B']=[x for x in Nums[8].difference(Nums[6])][0]
    chardict['A']=[x for x in Nums[7].difference(Nums[1])][0]
    chardict['D']=Nums[0].difference(Nums[7]).difference(Nums[4])
    chardict['D'].discard(chardict['E'])
    chardict['D']=[x for x in chardict['D']][0]
    chardict['C']=Nums[1]
    chardict['C'].discard(chardict['B'])
    chardict['C']=[x for x in chardict['C']][0]
    chardict['F']=[x for x in Nums[4].difference(Nums[3])][0]
    
    print('')
    print(' '*SPC,end='')
    for i in range(4):
        print(' ',end='')
        if int(nm[i]) in [0,2,3,5,6,7,8,9]:
            print(chardict['A']*3,'    ',end='')
        else:
            print('        ',end='')
    print('')
    for j in range(2):
        print(' '*SPC,end='')
        for i in range(4):
            if int(nm[i]) in [0,4,5,6,8,9]:
                print(chardict['F'],end='')
            else:
                print(' ',end='')
            print('   ',end='')
            if int(nm[i]) in [0,1,2,3,4,7,8,9]:
                print(chardict['B'],end='    ')
            else:
                print(' ',end='    ')
        print('')
    print(' '*SPC,end='')
    for i in range(4):
        print(' ',end='')
        if int(nm[i]) in [2,3,4,5,6,8,9]:
            print(chardict['G']*3,'    ',end='')
        else:
            print('        ',end='')
    print('')
    for j in range(2):
        print(' '*SPC,end='')
        for i in range(4):
            if int(nm[i]) in [0,2,6,8]:
                print(chardict['E'],end='')
            else:
                print(' ',end='')
            print('   ',end='')
            if int(nm[i]) in [0,1,3,4,5,6,7,8,9]:
                print(chardict['C'],end='    ')
            else:
                print(' ',end='    ')
        print('')
    print(' '*SPC,end='')
    for i in range(4):
        print(' ',end='')
        if int(nm[i]) in [0,2,3,5,6,8,9]:
            print(chardict['D']*3,'    ',end='')
        else:
            print('        ',end='')
    print('')
    
    time.sleep(0.01)
    


print("\u001b[2J\u001b[0;0H")
print("\u001b[?25l")
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
    tempmsg=msg
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
    printmsg(tempmsg,ret2str,trueNums)
    #print(ret2str,'|',ret2)

print("\u001b[?25h")
print("\nPart 1 result =",res1)        
print("Part 2 result =",ret2)
print("Done in {:.6f} s".format(time.time()-starttime))





                

