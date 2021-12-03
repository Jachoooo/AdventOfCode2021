#Advent od Code 2021
#JKL
INPUTFILE="input.txt"


depth1=0
position1=0
depth2=0
position2=0
aim2=0
inputFile=open(INPUTFILE,'r')
for line in inputFile:
    print(line,end='')
    line=line.split(" ")
    match line[0]:
        case "down":
            depth1+=int(line[1])
            aim2+=int(line[1])
        case "up":
            depth1-=int(line[1])
            aim2-=int(line[1])
        case "forward":
            position1+=int(line[1])
            position2+=int(line[1])
            depth2+=aim2*int(line[1])


print("\nPart 1 result = ",depth1*position1)
print("Part 1 result = ",depth2*position2)
inputFile.close()