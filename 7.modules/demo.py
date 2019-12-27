import calc
print(calc.pi)
print(calc.add(10,2))
print(calc.sub(10,2))
print(calc.multi(10,2))
print(dir(calc))


from calc import add,multi
print(add(10,2))
print(multi(10,2))


from calc import *
print(add(10,2))
print(sub(10,2))
print(multi(10,2))

from calc import multi as m
print(m(10,2))

import reverse
print(reverse.reverse(bhupendra))

def sum(a,b):
    c=a+b
    return c
print(sum(10,2))

def sub(a,b=5):
    c=a-b
    return c
print(sub(10))

def sub(a,b=5):
    c=a-b
    return c
print(sub(10,3))

def multi(a,b):
    c=a*b
    return c
print(multi(10,2))

def multi(a=10,b=2):
    c=a*b
    return c
print(multi())

def add(a,b):
    c=a+b
    return c
print(add(b=10,a=2))

def rec(n):
    if n==0:
        return 1
    print("printing value of ", n)
    n-=1
    rec(n)

from calc import add,multi
print(add(10,2))
print(multi(10,2))

from calc import *
print(add(10,2))
print(multi(10,2))
print(sub(10,2))

from calc import multi as m
print(m(10,4))

import calc from add
print(add(10,2))

