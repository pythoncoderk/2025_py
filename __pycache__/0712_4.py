def to_base(x, b):
    digs = []
    while x:
        digs.append(x % b)
        x //= b
    return digs  # 反転済み（下位→上位）

def is_palindrome(seq):
    return seq == seq[::-1]

def gen_palins(n):
    s = str(n)
    return int(s + s[-2::-1])  # 奇数桁
def gen_paline(n):
    s = str(n)
    return int(s + s[::-1])    # 偶数桁

def count_pal_both(N):
    ans = 0
    for length in range(1, 19):  # 最大18桁程度
        half = (length + 1) // 2
        start = 10**(half - 1)
        end = 10**half
        for prefix in range(start, end):
            if length % 2:
                x = gen_palins(prefix)
            else:
                x = gen_paline(prefix)
            if x > N:
                continue
            for b in range(2, 10):
                if is_palindrome(to_base(x, b)):
                    ans += 1
                    break
    return ans

print(count_pal_both(int(input())))
