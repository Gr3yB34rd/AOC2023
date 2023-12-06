import timeit
print("starting AOC03a")



input=open('input.txt','r')
Lines=input.readlines()
starttime = timeit.default_timer()
sum = 0

map = []
print("Length: "+str( len(Lines)))
for idx,line in enumerate(Lines):
    line = line.strip()
    row = [*line]
        
    
    row = ["."]+row+["."]
    if idx == 0:
        buffer = ["."] * len(row)
        map.append(buffer)
    map.append(row)
    if idx == len(Lines)-1:
        buffer = ["."] * len(row)
        map.append(buffer) 
#for row in map:
#    print(row)
#print("------------------------------------------------------------------")
sum = 0
for i,row in enumerate(map):
    numbers = []
    keep = False
    comp = False
    for j,sign in enumerate(row):
        if map[i][j].isnumeric():
            numbers.append(j)
            if (not map[i-1][j-1].isnumeric()) & (map[i-1][j-1] != "."):
                keep=True
            if (not map[i-1][j].isnumeric()) & (map[i-1][j] != "."):
                keep=True
            if (not map[i-1][j+1].isnumeric()) & (map[i-1][j+1] != "."):
                keep=True
            if (not map[i][j-1].isnumeric()) & (map[i][j-1] != "."):
                keep=True
            if (not map[i+1][j-1].isnumeric()) & (map[i+1][j-1] != "."):
                keep=True
            if (not map[i+1][j].isnumeric()) & (map[i+1][j] != "."):
                keep=True
            if (not map[i+1][j+1].isnumeric()) & (map[i+1][j+1] != "."):
                keep=True
            if (not map[i][j+1].isnumeric()): 
                 comp=True    
                 if (map[i][j+1] != "."):
                    keep = True
            if comp == True:
            #    print(numbers)
            #    print("---")
                if keep==False:
                    for x in numbers:
                        map[i][x] = "."
                else:
                    num =''
                    for x in numbers:
                        num = num+ str(row[x])       
                    print(num)
                    sum = sum+int(num)
                numbers=[]
                keep = False
                comp = False
#for row in map:
#    print(row)
print(sum)    
print("ending AOC03a")