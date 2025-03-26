l = ["a", "i", "u", "e", "o"]

s = input()
ans = ""
for i in s:
    if i not in l:
        ans += i

print(ans)