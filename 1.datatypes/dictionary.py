'''This is dictionary data type'''
d={'a':'apple','b':'banana','c':'carrot',2:'two'}
'''key:values
key=a,b,c
values=apple,banana,carrot'''
print(d)
'''print unique key 
'''
print(d[2])
print(d['a'])
print(d['c'])
d[2]=9999
print(d)

'''Usage

To find out any charater or number is available in it or not
and we can change values in set from dictionary e.g. line 10,11''' 

d={'a':'apple',2:'banana','m':'mango'}
print(d)

print(d['a'])
print(d.get(2))

d[2]='orange'
print(d)

d[3]='watermelon'
print(d)

d.update({1:'cherry','b':'grapes'})
print(d)

del d['a']
print(d)

d.pop(2)
print(d)

print(d.keys())

print(d.values())

print(d.items())

l=[10,3,23,37,33,5] 
sum=0
a=0
for x in l:
    if x>a:
        a=x
    sum+=x
print(sum)
print('maximum number from a list is',a)