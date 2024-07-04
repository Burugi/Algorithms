## 14889와 비슷한데 N이 짝수가 고정이 되어있지 않은 문제다 

from itertools import combinations

def calculate_team_score(team, S):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score

def solve(N, S):
    players = range(N)
    min_diff = float('inf')
    
    for i in range(1,(N//2)+1):
    # range(1, N)으로 하면 답은 나오는데 시간초과가 뜬다.
    # range(1, N/2)으로 중복된 팀을 구하지 않는게 좋다. -> pypy3로 돌려야 맞음
        for team in combinations(players, i):
            team1 = list(team)
            team2 = list(set(players) - set(team1))
            
            score1 = calculate_team_score(team1, S)
            score2 = calculate_team_score(team2, S)
            
            diff = abs(score1 - score2)
            if diff < min_diff:
                min_diff = diff
    
    return min_diff

# 입력 처리 부분
N = int(input().strip())
S = [list(map(int, input().split())) for _ in range(N)]

print(solve(N, S))
