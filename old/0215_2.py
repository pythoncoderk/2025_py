s, m = map(str, input().split())

if s == "sick" and m == "fine":
    print(2)
elif s == "sick" and m == "sick":
    print(1)
elif s == "fine" and m == "sick":
    print(3)
else:
    print(4)