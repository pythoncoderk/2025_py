

def t():
    for i in range(10):
        yield i

for i in t():
    print(i)