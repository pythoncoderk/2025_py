a, b = map(int, input().split())

print(a // b if a % b == 0 else (a // b) + 1)