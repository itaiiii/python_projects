L = [5,8,3,5,7,1,4,6,4,3,3,5,6,9,6]
counts_list = [0,0,0,0,0,0,0,0,0,0]

for i in L:
    counts_list[i]+=1
    
for i in range(10):
    print(i, " was found: ", counts_list[i])
    
    