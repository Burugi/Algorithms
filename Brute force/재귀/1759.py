from itertools import combinations

def is_valid(password):
    vowels=['a','e','i','o','u']
    vowels_count=sum(1 for char in password if char in vowels)
    consonant_count=len(password)-vowels_count
    return vowels_count>=1 and consonant_count>=2

def solve(L,C,chars):
    chars.sort()
    possible_password=combinations(chars,L)
    
    valid_passwords=[]
    for password in possible_password:
        # if is_valid(password):
        #     print(" ".join(password))
    # 여기까지만 쓰면 출력은 맞는데 각 패스워드마다 sort가 되어있지 않는 상태이기에 이를 묶어서 sort해줘야하는 구나
        if is_valid(password):
            valid_passwords.append("".join(password))
    
    valid_passwords.sort()
    for password in valid_passwords:
        print(password)


L, C = map(int,input().strip().split())
chars = input().strip().split()

solve(L,C,chars)