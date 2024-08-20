L = [1,2,3,4,5,6,7,8,-200,9,10]
positive_indexes = []
possible_sums = []


for i in range(len(L)):
    if L[i] > 0:
        positive_indexes.append(i)

for i in range(len(positive_indexes)):
    for j in range(1,len(positive_indexes)):
        if(j>=i):
            start = positive_indexes[i]
            end = positive_indexes[j]
            possible_sums.append(sum(L[start:end+1]))

        
        
print(max(possible_sums))

        