# 入力を受け取る
n = int(input())
a = [int(x) for x in input().split()]

# 答えを保存する変数を用意して適切な初期値で初期化
mi = 100
ma = -100

# 配列(リスト)の全要素をチェックするループを書いて

for i in a:
    if i < mi:
        mi = i
    if i > ma:
        ma = i

# 暫定maxを更新
# 暫定minを更新

# 答えを出力する
print(ma, mi)