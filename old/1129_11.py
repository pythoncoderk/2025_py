H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# 上下左右4方向
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

# 結果を書き込む用の別配列（元を壊さない）
res = [['' for _ in range(W)] for _ in range(H)]

for y in range(H):
    for x in range(W):
        # # はそのまま
        if grid[y][x] == '#':
            res[y][x] = '#'
            continue

        # 空き地 . の場合、周囲4方向を調べる
        cnt = 0
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            # 境界チェック
            if 0 <= ny < H and 0 <= nx < W:
                if grid[ny][nx] == '#':
                    cnt += 1

        # 数字に置き換え
        res[y][x] = str(cnt)

# 出力
for y in range(H):
    print("".join(res[y]))
