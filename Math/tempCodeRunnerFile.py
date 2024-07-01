'''
n^2까지는 될 것 같다.
'''
def sumOfNum(a):
    sum=0
    for i in range(1,a+1):
        if a%i==0:
            sum+=i
            
    return sum

num = input()
total_sum=0
for i in range(int(num)):
    total_sum+=sumOfNum(i+1)
print(total_sum)