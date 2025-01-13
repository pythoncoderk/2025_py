n = int(input())

ans = hex(n)[2:]

final = ""
for i in ans:
    if i.isdigit():
        final += i
    else:
        final += i.upper()

print(final.zfill(2))
