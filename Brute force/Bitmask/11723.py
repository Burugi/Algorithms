# 11723번

import sys

m = int(sys.stdin.readline())
S = set()
# readline이 좀더 빠르다. -> read로 하지 말기
# 그 외에는 뭐가 다른지 정확하니느 모르겠다.
for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

# import sys
# input = sys.stdin.read

# commands = input().split()
# m = int(commands[0])
# S = 0

# idx = 1
# result = []
# for _ in range(m):
#     cmd = commands[idx]
    
#     if cmd == "add":
#         x = int(commands[idx + 1])
#         S |= (1 << x)
#         idx += 2
#     elif cmd == "remove":
#         x = int(commands[idx + 1])
#         S &= ~(1 << x)
#         idx += 2
#     elif cmd == "check":
#         x = int(commands[idx + 1])
#         if S & (1 << x):
#             result.append("1")
#         else:
#             result.append("0")
#         idx += 2
#     elif cmd == "toggle":
#         x = int(commands[idx + 1])
#         S ^= (1 << x)
#         idx += 2
#     elif cmd == "all":
#         S = (1 << 21) - 1
#         idx += 1
#     elif cmd == "empty":
#         S = 0
#         idx += 1

# sys.stdout.write("\n".join(result) + "\n")
