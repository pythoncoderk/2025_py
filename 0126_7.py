x, y, n = map(int, input().split())

direction = ["E", "S", "W", "N"]

now_direction = 0
max_direction = 1
direction_count = 0
flag = True
for i in range(n):
    if direction[now_direction % 4] == "N":
        y -= 1
        direction_count += 1
        now_direction += 1
    elif direction[now_direction % 4] == "E":
        x += 1
        direction_count += 1
        now_direction += 1
    elif direction[now_direction % 4] == "S":
        y += 1
        direction_count += 1
        now_direction += 1
    elif direction[now_direction % 4] == "W":
        x -= 1
        direction_count += 1
        now_direction += 1

    if max_direction == direction_count and flag:

        flag = False
    else:




print(x, y)