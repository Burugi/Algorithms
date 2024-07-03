import sys
input = sys.stdin.read

'''
def backtrack(현재 상태, 선택지):
    if 종료 조건:
        해를 찾았으므로 기록 또는 반환
    else:
        for 선택 in 선택지:
            현재 선택이 유효한지 확인
            if 유효하다면:
                선택을 상태에 반영
                backtrack(갱신된 상태, 선택지)
                상태를 이전으로 복원
'''


def backtracking(n,m,depth,path,used,results):
    if depth==m:
        results.append(path[:])
        return
    # 마치 될때까지 돌아가는 걸 구하는 거구나. 복잡도가 굉장히 높음 
    # N, M이 굉장히 작은 수라서 가능한 거구나 
    for i in range(1,n+1):
        if not used[i]:
            used[i]=True
            path.append(i)
            backtracking(n,m,depth+1,path,used,results)
            path.pop()
            used[i]=False
            
def solve(n,m):
    results=[]
    used=[False] *(n+1)
    backtracking(n,m,0,[],used,results)
    for result in results:
        print(' '.join(map(str,result)))
    

input_data = input().strip().split()
n, m = int(input_data[0]),int(input_data[1])

solve(n,m)
