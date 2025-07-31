def main():
    S = input().strip()
    positions = [i + 1 for i, ch in enumerate(S) if ch == '#']

    # 2つずつ出力
    for i in range(0, len(positions), 2):
        # 安全性のため、次の要素が存在するかチェック
        if i + 1 < len(positions):
            print(f"{positions[i]},{positions[i+1]}")

if __name__ == "__main__":
    main()