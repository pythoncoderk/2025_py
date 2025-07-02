s = input()

x = "1"
count = 2
while True:
    x += "0"
    if s == x:
        print(count)
        break
    kari = ""
    for i in range(len(x)):
        if x[i] == "9":
            kari += "1"
            count += 1
        else:
            kari += str(int(x[i]) + 1)
            count += 1
    x = kari
    if x == s:
        print(count)
        break