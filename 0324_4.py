n1 = ["鈴木", "斎藤", "田中"]
n2 = ["めい", "ゆづき", "ひなた"]
result = list(map(lambda x, y: x + y + " さん", n1, n2))
print(result)