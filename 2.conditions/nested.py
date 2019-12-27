num=int(input("Enter any number"))
'''This condition is use for nested type'''
if num >0:
    if num%2==0:
        print(num,"is a positive even number")
    else:
        print(num, "is a positive odd number")
elif num <0:
    print(num, "is a negative number")
else:
    print(num, "is a zero")