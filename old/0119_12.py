# 入力を受け取る
n = int(input())
a = [int(x) for x in input().split()]

# 答えを保存する変数を用意して0で初期化

ind = 0
for i in range(n):
    if a[i] % 2 == 0:
        ind = i + 1
        break
print(ind)
# 配列(リスト)の全要素をインデックス付きでiterateするループを書いて
# 要素が偶数かどうか判定して
# 偶数だったらインデックスを保存してループを抜ける

# 答えを出力する
