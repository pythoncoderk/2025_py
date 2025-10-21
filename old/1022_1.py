a, b = map(str, input().split())
s = input()
n, m = map(int, input().split())

x = s[n+len(a)-1:m-1]

print("<blank>" if len(x) == 0 else x)