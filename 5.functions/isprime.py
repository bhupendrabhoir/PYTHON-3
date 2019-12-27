def isprime(num):
    '''
        This function is usefull to find numbers are prime or not
    '''
    count=0
    for i in range(2,num):
        if num%i==0:
            count+=1
    if count==0:
        print(num, "is prime")
    else:
        print(num, "is not prime")
