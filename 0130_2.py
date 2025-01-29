l = ["a", "e", "i", "o", "u"]
s = input()

ans = ""

for j in s:
    if j not in l:
        ans += j

print(ans)