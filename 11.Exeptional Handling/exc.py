'''This program is 
for exeptional Handling
with try, except and finally blocks'''


def divby(a,b):
    return a/b
    
try:
    print(divby(10,2))
    print(divby(10,3))
    print(divby(10,0))
    print(divby(10,4))
    print("This won't execute")
    
except:
    print("Can not divide with Zero")
    
finally:
    print("This statemen always execute")
    

def divby(a,b):
    return a/b
    
try:
    print(divby(10,2))
    print(divby(10,3))
    print(divby(10,'a'))
    print(divby(10,4))
    print("This won't execute")
    
except ZeroDivisionError:
    print("Can not divide with Zero")
except TypeError:
    print("Can not divide with string")
finally:
    print("This statemen always execute")
    

def divby(a,b):
    return a/b
    
try:
    print(divby(10,2))
    print(divby(10,3))
    print(divby(10,a))
    print(divby(10,4))
    print("This won't execute")
    
except:
    print("Can not divide with Zero")
except TypeError:
    print("Can not divide with string")
except:
    print("syn tax")
finally:
    print("This statemen always execute")