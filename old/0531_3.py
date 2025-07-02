n, m = map(int, input().split())
set_l = set(i for i in range(1, n + 1))

l = []
for i in range(m):
    x, y = map(int, input().split())
    set_i = set()
    for i in range(x, y+1):
        set_i.add(i)

    l.append(set_i)

# print(n, m)
# print(set_l)
# print(l)

final_set = set()
for i in range(m):
    set_w = l[i]
    for j in range(m):
        if i != j:
            set_w = set_w - l[j]
    if len(set_w) >= 1:
        for q in set_w:
            final_set.add(q)
if len(final_set) < n:
    print(0)
    exit()
ans_ans = final_set.pop()
for i in range(len(l)):
    if ans_ans in l[i]:
        print(i + 1)
        exit()

print(0)

