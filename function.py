import math

def fun1(a):
    def fun2(b):
        f = a * math.pow(b, a)
        l = f"Для значений {a},{b} функция f(a,b) = {f}"
        return l

    return fun2