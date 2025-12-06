import itertools

n  = int(input())
l = list(map(int, input().split()))

nums = range(1, n+1)
l2 = list(itertools.combinations(nums, 2))



fin = 0
for i in l2:
    sum = 0
    ans = 0
    for j in range(i[0]-1,i[1]):
        sum += l[j]
    for k in range(i[0]-1, i[1]):
        if sum % l[k] == 0:
            ans += 1

    if ans == 0:
        fin += 1

print(fin)
