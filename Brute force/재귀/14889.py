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
    
    for team in combinations(players, N//2):
        team1 = list(team)
        # 이렇게 set으로 조합을 빼는 게 가능하구나 
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
