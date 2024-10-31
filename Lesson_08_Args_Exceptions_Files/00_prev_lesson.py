def some_func(a):
    if a > 10:
        return True
    if a < 100:
        return True

    if a + 1 == 5:
        return True
    else:
        return False


def some_func_optimized(a):
    if (100 > a > 10) and (a + 1 == 5):
        return True
    else:
        return False


def some_func_optimized2(a):
    if (100 > a > 10) and (a + 1 == 5):
        return True
    return False


def some_func_optimized3(a):
    return True if (100 > a > 10) and (a + 1 == 5) else False


def some_func_optimized4(a):
    return (100 > a > 10) and (a + 1 == 5)


def max_val(w, x, y, z):
    if w >= x and w >= y and w >= z:
        print('w')


w1, x1, y1, z1 = 100, 200, 40, 300
max_val(w1, x1, y1, z1)
