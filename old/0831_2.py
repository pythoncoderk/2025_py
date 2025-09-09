a, b = map(int,input().split())
print(a + b)

c = int(input())
d = int(input())
print(c + d)


e, f = map(str,input().split())
print(e if len(e) > len(f) else f)

g, h = map(str,input().split())
print(g if len(g) > len(h) else h)

i, j = map(str,input().split())
if len(i) == len(j):
    print("onaji")
elif len(i) > len(j):
    print(i)
else:
    print(j)