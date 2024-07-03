# 순열을 이용한 간단한 풀이
# from itertools import combinations

heights = [int(input()) for _ in range(9)]

# for combination in combinations(heights,7):
#     if sum(combination)==100:
#         result=sorted(combination)
#         break
    

# # 반복문 2번을 이용한 풀이 -> 될 것 같은데 안되네
total_sum=sum(heights)
heights.sort()
def aa(heights, total_sum):
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            if (total_sum-heights[i]-heights[j])==100:
                # heights.pop(i) # 이렇게 순서대로 pop하면 인덱스가 바뀌면서 안된다. 
                # heights.pop(j) 
                return i,j
i,j=aa(heights, total_sum) 
# 마구잡이식 문제풀이로 풀었다.
for value in heights:
    if value !=heights[i] and value !=heights[j]:
        print(value)
