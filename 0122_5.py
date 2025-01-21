l = ["and", "not", "that", "the", "you"]

n = int(input())

l2 = list(map(str, input().split()))

for i in l2:
    if i in l:
        print("Yes")
        exit()
print("No")

