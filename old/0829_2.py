n, m = map(int, input().split())
l = list(map(str, input().split()))


flag = True
for i in range(m-1):


    if l[i][len(l[i]) - n:] != l[i+1][:n]:
        flag = False

print("YES" if flag else "NO")