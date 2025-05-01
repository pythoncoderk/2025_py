def solve():
    tag_a, tag_b = input().split()
    search_str = input()
    p = 0
    s = 0
    while True:
        s = search_str[p::].find(tag_a)
        p += s + len(tag_a)
        e = search_str[p::].find(tag_b) + p
        if s == -1:
            break
        elif p == e:
            print('<blank>')
        elif p < e:
            print(search_str[p:e:])
        p = e
if __name__ == "__main__":
    solve()