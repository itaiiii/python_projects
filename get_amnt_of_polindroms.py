num = input("number: ")
counter = 0
while int(num)>=0:
    length = len(num)
    right = ""
    left = ""
    if length!= 1:
        for i in range(length):
            left+=num[i]
            right+=num[length-1-i]
        
        if left == right:
            counter+=1
    else:
        counter+=1
        
    num = input("number: ")
    
print(counter)