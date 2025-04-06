n = int(input())
l = list(map(int, input().split()))
q = int(input())
l2 = [list(map(int, input().split())) for i in range(q)]

# print(n)
# print(l)
# print(q)
# print(l2)

for i in range(q):
    l[l2[i][0]-1], l[l2[i][1]-1] = l[l2[i][1]-1], l[l2[i][0]-1]

for i in range(n-1):
    if l[i] > l[i+1]:
        print("No")
        exit()

print("Yes")