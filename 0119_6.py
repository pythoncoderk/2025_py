n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

# 答えを保存する変数を用意して0で初期化
count = 0
# 配列(リスト)の全要素をチェックするループを書いて
for i in a:
    if k == i:
        count += 1
# 要素がkと一致しているか判定して
# 一致していたら答えをインクリメント

# 答えを出力する
print(count)
