a, b, c, d, e, f, x = map(int, input().split())

t_count = 0
t_time = 0
flag = "a"
while True:
    if flag == "a":
        if t_time + a <= x:
            t_count += a
            t_time += a
            flag = "b"
        elif x - t_time >= 0:
            t_count += x - t_time
            break
    else:
        if t_time + c <= x:
            t_time += c
            flag = "a"
        else:
            break

a_count = 0
a_time = 0
flag = "a"
while True:
    if flag == "a":
        if a_time + d <= x:
            a_count += d
            a_time += d
            flag = "b"
        elif x - a_time >= 0:
            a_count += x - a_time
            break
    else:
        if a_time + f <= x:
            a_time += f
            flag = "a"
        else:
            break

if t_count * b > a_count * e:
    print("Takahashi")
elif t_count * b < a_count * e:
    print("Aoki")
else:
    print("Draw")