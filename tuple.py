point=(4,10)
print(type(point))
print(point[0])

#point[0]=5


def add_mul(a,b):
    total = a+b
    mul = a*b
    return total, mul

s,m =add_mul(5,10)
print(s)
print("And")
print(m)