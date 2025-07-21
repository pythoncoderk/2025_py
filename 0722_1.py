s = list(input())
s_count = s.count(".")
s_len = len(s)
count = 2
i = 0
while s_len != s_count:
    if s[i] == "#":
        if count == 2:
            print(str(i + 1) + ",", end="")
            s[i] = "."
            count -= 1
        else:
            print(i + 1)
            s[i] = "."
            count = 2
    else:
        i += 1
        s_count = s.count(".")
        s_len = len(s)
