n =int(input())
arr=list(map(int,input().split()))
# 다음 순열 구하는 공식이 이건데 수학적으로 이해는 가지 않아서 그냥 외운다
def permutation(arr):
    n=len(arr)
    i=n-1
    
    while i>0 and arr[i-1]<=arr[i]:
        i-=1
    
    if i<=0:
        return False
    
    j=n-1
    while arr[j]>=arr[i-1]:
        j-=1
        
    arr[i-1],arr[j]=arr[j],arr[i-1]
    
    arr[i:]=arr[i:][::-1]
    return True

if permutation(arr):
    print(' '.join(map(str,arr)))
else:
    print(-1)