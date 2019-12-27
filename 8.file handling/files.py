'''import os
print(os.getcwd())
# print(os.listdir())
# os.mkdir("myfolder")
# print("myfolder created")
# os.mkdir("myfolder/test")
# print("test folder created")
os.chdir("c://file handling/my folder")
print(os.getcwd())'''

# content='''This is my
# new content to 
# write in file
# '''
filename="myfolder/demo.txt"
# f=open(filename,"w")
# f.write(content)
# print("writing done")
# f.close()

# content='''This is my
# appended content to 
# write in file
# i done
# '''
# filename="myfolder/demo.txt"
# f=open(filename,"a")
# f.write(content)
# print("writing is done")
# f.close()

f=open(filename,'r')
# data=f.read()
# data=f.read(10)
# data=f.readlines()
data=f.readline()
print(data)
f.close()