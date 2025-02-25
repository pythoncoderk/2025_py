def outer(a, b):

    def puls(c, d):
        return c + d
    r = puls(a, b)
    print(r)

outer(1, 2)