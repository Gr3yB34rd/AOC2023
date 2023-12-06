import timeit
print("starting AOC03a")



input=open('input.txt','r')
Lines=input.readlines()



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
    copymap =[]    
for row in map:
    ones = [1]*len(row)
    copymap.append(ones)
    print(row)
print("------------------------------------------------------------------")
for row in copymap:
    print(row)
print("-------------------------------------------------------------------")    
for i,row in enumerate(map):
    numbers = []
    keep = False
    comp = False
    ipos,jpos = 0,0
    for j,sign in enumerate(row):
        if map[i][j].isnumeric():
            numbers.append(j)
            if (not map[i-1][j-1].isnumeric()) & (map[i-1][j-1] == "*"):
                ipos = i-1
                jpos = j-1
                keep=True
            if (not map[i-1][j].isnumeric()) & (map[i-1][j] == "*"):
                ipos = i-1
                jpos = j
                keep=True
            if (not map[i-1][j+1].isnumeric()) & (map[i-1][j+1] == "*"):
                ipos = i-1
                jpos = j+1
                keep=True
            if (not map[i][j-1].isnumeric()) & (map[i][j-1] == "*"):
                ipos = i
                jpos = j-1
                keep=True
            if (not map[i+1][j-1].isnumeric()) & (map[i+1][j-1] == "*"):
                ipos = i+1
                jpos = j-1
                keep=True
            if (not map[i+1][j].isnumeric()) & (map[i+1][j] == "*"):
                ipos = i+1
                jpos = j
                keep=True
            if (not map[i+1][j+1].isnumeric()) & (map[i+1][j+1] == "*"):
                ipos = i+1
                jpos = j+1
                keep=True
            if (not map[i][j+1].isnumeric()): 
                 comp=True    
                 if (map[i][j+1] == "*"):
                    ipos = i
                    jpos = j+1
                    keep = True
            if comp == True:
            #    print(numbers)
            #    print("---")
                if keep==False:
                    for x in numbers:
                        map[i][x] = "."
                    ipos = 0
                    jpos = 0    
                else:
                    num =''
                    for x in numbers:
                        num = num+ str(row[x])       
                  #  print(num)
                    copymap[ipos][jpos] *= -int(num)
                numbers=[]
                keep = False
                comp = False
                ipos = 0
                jpos = 0
sum = 0
for row in copymap:
    for element in row:
        if element > 1:
            sum += element
print(sum)    
print("ending AOC03a")