user = int(input('Enter num'))
list = [0,1]
for i in range(1, (user-1)):
    list.append(list[i]+list[i-1])
    
print(list)