n, c = map(int, input().split())
l = list(map(int, input().split()))

count = 0
times = 0
for i in l:
    if times == 0:
        count += 1
        times = i
    elif i - times >= c:
        count += 1
        times = i
    else:
        pass

print(count)




