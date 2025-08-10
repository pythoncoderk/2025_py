import sys

def main():
    # N, Q を読み取り
    N, Q = map(int, sys.stdin.readline().split())

    # 'A'.. の初期列を作成
    s = [chr(ord('A') + i) for i in range(N)]

    # バブルソート風に、隣り合う要素をクエリして入れ替え
    for i in range(N):
        for j in range(N - 1):
            print(f"? {s[j]} {s[j+1]}", flush=True)
            ans = sys.stdin.readline().strip()
            if ans == '>':
                s[j], s[j+1] = s[j+1], s[j]

    # 最終結果を出力
    print(f"! {''.join(s)}", flush=True)

if __name__ == "__main__":
    main()