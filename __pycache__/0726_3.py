l = list(input())
s_count = l.count("#")
t_count = l.count(".")

# print(s_count)
# print(t_count)

if s_count == 0 and t_count >= 2:
    for i in range(len(l)):
        if l[i] == ".":
            l[i] = "o"
            break
else:
    for i in range(s_count):
        for j in range(len(l)-1, -1, -1):
            if l[j] == ".":
                l[j] = "o"
                break

for i in range(len(l)):
    if i == 0:


print("".join(l))