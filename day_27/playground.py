def add(*args):
    s = 0
    for n in args:
        s += n
    return s 

print(add(2,3,5,8,10,6,8,10,2,55,20))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)