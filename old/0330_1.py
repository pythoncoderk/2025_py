import sys


def main():
    # 入力の読み込み
    H, W, N = map(int, sys.stdin.readline().split())
    stamps = []

    # スタンプのデータを取得
    for _ in range(N):
        stamp = [sys.stdin.readline().strip() for _ in range(H)]
        stamps.append(stamp)

    # R, C の取得
    R, C = map(int, sys.stdin.readline().split())
    art_plan = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

    # アートの構築
    result = []
    for i in range(R):
        temp_rows = ["" for _ in range(H)]  # H行分のリストを作成
        for j in range(C):
            stamp_index = art_plan[i][j] - 1  # 1-based index を 0-based index に
            for k in range(H):
                temp_rows[k] += stamps[stamp_index][k]  # 横方向に結合
        result.extend(temp_rows)  # 縦方向に追加

    # 出力
    sys.stdout.write("\n".join(result) + "\n")