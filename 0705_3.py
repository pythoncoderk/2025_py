from collections import deque

n = int(input())
q = deque()
for i in range(n):
    q2 = deque(map(int, input().split()))
    if q2[0] == 1:
        for j in range(q2[1]):
            q.append(q2[2])
    else:
        total = 0
        for k in range(q2[1]):
            total += q.popleft()
        print(total)