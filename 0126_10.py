l = list(map(str, input().split()))

for i in l:
    if i == "red":
        print("Yes")
        exit()
print("No")