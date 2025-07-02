n, q = map(int, input().split())
l = list(map(int, input().split()))
box = [0] * n
ans = []
for i in range(q):
    min_l = min(box)
    for j in range(q):
        if l[i] != 0:
            box[l[i]-1] += 1
            ans.append(l[i])
            break
        else:
            if box[j] == min_l:
                box[j] += 1
                ans.append(j+1)
                break
print(*ans)

