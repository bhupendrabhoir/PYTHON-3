'''
This is user exception
where we can raise exception'''

class ValueNeagative(Exception):
    pass
class ValueZero(Exception):
    pass
    
num = int(input("Enter positive number:"))
try:
    if num == 0:
        raise ValueZero("Zero value not allowed")
    elif num<0:
        raise ValueNeagative
    else:
        print(num,"is positive")
except ValueZero as msg:
    print(msg)
except ValueNeagative:
    print("Negative value are allowed")