target = int(input())
broken_cnt=int(input())

"""
1. 런타임 에러 오류
이거는 입력에서 문제가 생기는 것이므로 게시판을 보니 고장난 것이 없을 때,
세번째 줄의 입력을 문제 삼기 때문이다.
따라서 순서를 변경하니 해결됨  
"""

if broken_cnt==0:
    broken_buttons=set() # 그냥 빈 집합, 순서에 상관없으니 만들어두는 것 
    # 
else:
    broken_num=input().strip().split()
    broken_buttons=set(broken_num)

def is_possible_clicks(channel,broken_buttons):
    for digit in str(channel):
        if digit in broken_buttons:
            return False
    return True
# 일단 한번에 가능한지 확인하는 것
def find_min_clicks(target,broken_buttons):
    min_clicks=abs(target-100)
    
    for channel in range(1000001):
        if is_possible_clicks(channel,broken_buttons):
            clicks=len(str(channel))+abs(channel-target)
            # 이게 키워드다. 반복문 하나정도는 크게 둬도 상관없음을 확인할 수 있다.
            # 일단은 제일 가까운 채널을 찾아가면서 차이는 채널과 타겟의 차이는 +혹은 -만큼 진행되는 것을 알수 있으니...
            min_clicks=min(clicks,min_clicks)
    return min_clicks
    
print(find_min_clicks(target,broken_buttons))