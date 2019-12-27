'''This is datatype of String'''
str='Hello world'
print(str)

str="abc"
print(str)

str=2
print(str)

str='''i love python
its very interesting
i will make very nice career in it'''
print(str)

print(str[25])

print(str[2])

print(str[2:8])

print(str[2:])

print(str[:])

print(str.lower())

print(str.upper())

newstr=str.replace('world','user')
print(newstr)

l=str.split(" ")
print(l)

jstr=",".join(['apple','banana','mango'])
print(jstr)

name='virat'
othername='rohit'
print("Indian captain is {} and vice captain is {}".format(name,othername))

print(str.find('world'))