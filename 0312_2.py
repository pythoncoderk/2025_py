import re

n, m = map(str, input().split())
s = input()

print(n, m)

x = re.findall(fr"{n}.*{m}", s)

ans = []
n_len = len(n)
m_len = len(m)

for i in x:
    # print(i[n_len:n_len + m_len - 1], "これ")
    if i[n_len:n_len + m_len - 1] != "" and "<" not in i[n_len:n_len + m_len - 1] and ">" not in i[n_len:n_len + m_len - 1]:
        ans.append(i[n_len:n_len + m_len - 1])

if not ans:
    print("<blank>")
    exit()

for i in ans:
    print(i)