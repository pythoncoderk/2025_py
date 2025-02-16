n = input()

now_int = n[0]
for i in range(1, len(n)):
    if n[i] < now_int:
        now_int = n[i]
    else:
        print("No")
        exit()
print("Yes")