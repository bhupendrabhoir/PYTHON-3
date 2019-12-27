'''
This program is for
raise block using in
exceptional handling'''

def divby(a,b):
    if b == 0:
        raise ZeroDivisionError("Can not divide by zero")
    return a/b
    
try:
    print(divby(10,3))
    print(divby(10,2))
    print(divby(10,4))
    print(divby(10,0))

except ZeroDivisionError as msg:
    print(msg)
    
def divby(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b
    
try:
    print(divby(10,3))
    print(divby(10,2))
    print(divby(10,4))
    print(divby(10,0))

except ZeroDivisionError:
    print("Can not divide by zero")