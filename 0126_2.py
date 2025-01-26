x, y, n = map(int, input().split())

no = "E"
lr = 0

for i in range(1, n+1):
    if no == "E":
        x += 1
        lr += 1
    elif no == "W":
        x -= 1
        lr += 1
    elif no == "N":
        y -= 1
        lr += 1
    elif no == "E":
        y += 1
        lr += 1

    if i == lr:
        lr += 1
        if no == "E":
            no = "S"
        elif no == "S":
            no = "W"
        elif no == "W":
            no = "N"
        elif no == "N":
            no = "E"

