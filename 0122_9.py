n = int(input())

s = input()

flag = False

for i in s:
    if i == "|":
        if flag == False:
            flag = True
        else:
            flag = False
    if i == "*" and flag:
        print("in")
        exit()
print("out")
