a, b, c = map(int, input().split())

if a + b == c or a + c == b or b + c == a or a == b == c:
    print("Yes")
else:
    print("No")