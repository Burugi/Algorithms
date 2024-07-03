N = int(input().strip())

def count_digit(n):
    length = 0
    start =1
    digit=1 
    
    while start <= n:
        end= start*10-1
        if end > n:
            end = n
        length+=(end-start+1)*digit
        start*=10
        digit+=1
    return length

print(count_digit(N))
    