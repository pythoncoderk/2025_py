n = int(input())
s = input()

ans_s = ""

for i in s:
    if i == "p" or i == "a" or i == "i" or i == "z":
        ans_s += i

for i in range(n):
    if i == "p":
