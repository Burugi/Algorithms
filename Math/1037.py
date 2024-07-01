cnt = input()
list =[]
tmp=input().split()

for value in tmp:
    list.append(int(value))

if cnt!=1:    
    list.sort()
    print(list[0]*list[-1])
else:
    print(list[0]*list[0])
