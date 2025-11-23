n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort()
j = 0
flag = False
for i in l1:
    #print(i)
    if j >= len(l2):
        print("NO")
        flag = True
        break
    while True:
        if i <= l2[j]:
            j += 1
            break
        else:
            j += 1
if flag == False:
    print("YES")

