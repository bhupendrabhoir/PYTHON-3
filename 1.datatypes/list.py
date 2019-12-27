'''This is list Datatype'''
l=[10,3.5,'abc',True,[1,2,4],'xyz']
print(l)
print(l[1])
print(l[4])
print(l[4][1])
l[2]=999
print(l)


l=[10,3.5,'abc',4.5,20,'xyz']
print(l)
print(l[1])
print(l[1:5])
print(l[1:])
print(l[:])

l[3]=34
print(l)

l[2:4]=['def',3.7]
'''
To get all elements between 
2 to 4 index
not last element will be 
shown
'''
print(l)

l.append('a')
'''
to add 
single thing
in list'''
print(l)

l.extend(['b','c'])
'''
to add multiple
elements 
in list
'''
print(l)

l.insert(2,'apple')
'''
to insert any 
elementsat specific
place or index
'''
print(l)

del l[1]
print(l)

del l[2:4]
print(l)

del l
l.clear()

l.pop()
print(l)

l.pop(0)
print(l)

print(['a','b','c']+[1,2,3,4,5])

lis=[10,5,33,21,30]

lis.sort()
print(lis)

lis.reverse()
print(lis)

print(l.index('xyz'))
print(l.count('xyz'))