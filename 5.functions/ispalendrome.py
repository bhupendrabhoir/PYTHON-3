def ispalindrome(n):
    '''
        This function is state that number is palindrome or not
    '''
    rev=0
    x=n
    while n>0:
        mod=n%10
        n=n//10
        rev=rev*10+mod
    print(rev)
    if x==rev:
        print(x, "is a palindrome")
    else:
        print(x, "is not a palindrome")
