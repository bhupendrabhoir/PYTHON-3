'''This function is use in for loop with range'''
for x in range(1,10,1):
    print(x)
else:
    print("loop ended here")
    
for a in range(5):
    print(a)

a=["python","java","c++"]    
resume=input("Enter your skills")
while resume in a:
    print("resume is accepted")
    break