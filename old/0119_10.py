n = int(input())
a = [int(x) for x in input().split()]

index_of_even = 0
for i in range(n):
    if a[i] % 2 == 0:
        # インデックスを保存してループを抜ける
        index_of_even = i + 1
        break

print(index_of_even)