a = int(input())
b = int(input())
l = list(map(int, input().split()))

for i in range(len(l)):
    if l[i] == b:
        print()

c = int(input())
s = input()
d = int(input())
print(s[:c])
print(s[:d])
