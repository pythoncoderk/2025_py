s1, s2 = map(str, input().split())

if s1 == "fine" and s2 == "fine": print(4)
if s1 == "fine" and s2 == "sick": print(3)
if s1 == "sick" and s2 == "fine": print(2)
if s1 == "sick" and s2 == "sick": print(1)