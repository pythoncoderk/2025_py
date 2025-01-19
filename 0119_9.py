# 入力を受け取る
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

# 答えを保存する変数を用意して0で初期化
ind = 0

# 配列(リスト)の全要素をインデックス付きでiterateするループを書いて
for i in range(n):
    if a[i] == k:
        ind = i + 1
        break
print(ind)
# 要素がkと一致しているか判定して
# 一致していたらインデックスを保存してループを抜ける

# 答えを出力する
