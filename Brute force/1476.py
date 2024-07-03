# E, S, M = map(int, input().split())
# # 다중 입력 받는 방법
# year =1 
# while True:
#     if year%15==E and year%28==S and year%19==M:
#         break
#     year+=1
# print(year)
"""
위의 코드는 시간초과뜸 -> 맞았는데 뜨는게 아니고 애초에 틀린거구나 
예를 들면 S가 28으로 입력되었다면 실제로는 28이 아니고 0과 같은 것을 찾기때문에 빼고 나서 해야하는 게 맞다
"""
E, S, M = map(int, input().split())

year = 1
while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        break
    year += 1

print(year)
