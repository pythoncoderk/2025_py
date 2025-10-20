s1, s2 = map(str, input().split())
st = input()

f = 0
e = 0

while True:
    x_str = st[f:]
    x_s = x_str.find(s1) + len(s1)
    y_s = x_str.find(s2)

    if x_s == -1 or y_s == -1:
        break

    if x_s == y_s:
        print("<blank>")
    else:
        print(x_str[x_s:y_s])
    f += y_s + len(s2)

