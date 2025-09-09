n = int(input())
l = list(map(int, input().split()))

l2 = []

for i in range(n-1):
    l2.append(l[i+1] - l[i])

s2 = set(l2)
print("Yes" if len(s2) == 1 else "No")

l3 = []

for i in range(n-1):
    l3.append(l[i+1] / l[i])

s3 = set(l3)
print("Yes" if len(s3) == 1 else "No")