# 백트랙킹 생각보다 정말 쉽지 않다.
# 다만 한번 해보고 다시 돌아와서 보는 건 알게 되었다. 
def check(idx, current_sequence, S, N):
    total = 0
    for i in range(idx, -1, -1):
        total += current_sequence[i]
        sign = S[i][idx]
        if sign == '+' and total <= 0:
            return False
        if sign == '0' and total != 0:
            return False
        if sign == '-' and total >= 0:
            return False
    return True

def solve(N, S):
    current_sequence = [0] * N
    
    def backtrack(idx):
        if idx == N:
            print(' '.join(map(str, current_sequence)))
            return True
        
        for num in range(-10, 11):
            current_sequence[idx] = num
            if check(idx, current_sequence, S, N):
                if backtrack(idx + 1):
                    return True
        return False
    
    backtrack(0)

# 입력 처리 부분
N = int(input().strip())
signs = input().strip()

# S 배열 생성
S = [[''] * N for _ in range(N)]
index = 0
for i in range(N):
    for j in range(i, N):
        S[i][j] = signs[index]
        index += 1

solve(N, S)
