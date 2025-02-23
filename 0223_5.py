n, d = map(int, input().split())
s = input()

cookie = s.count("@")
print(n - (cookie - d))