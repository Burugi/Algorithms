
def is_valid(sequence, signs):
    for i in range(len(signs)):
        if signs[i] == '<' and sequence[i] > sequence[i + 1]:
            return False
        if signs[i] == '>' and sequence[i] < sequence[i + 1]:
            return False
    return True

def solve(k, signs):
    max_result = ""
    min_result = ""
    used = [False] * 10
    
    def backtrack(idx, current_sequence):
        nonlocal max_result, min_result
        if idx == k + 1:
            if is_valid(current_sequence, signs):
                num_str = ''.join(map(str, current_sequence))
                if not min_result or num_str < min_result:
                    min_result = num_str
                if not max_result or num_str > max_result:
                    max_result = num_str
            return
        
        for num in range(10):
            if not used[num]:
                used[num] = True
                current_sequence.append(num)
                backtrack(idx + 1, current_sequence)
                current_sequence.pop()
                used[num] = False

    backtrack(0, [])
    return min_result, max_result

# 입력 처리 부분
k = int(input().strip())
signs = input().split()

min_result, max_result = solve(k, signs)
print(max_result)
print(min_result)
