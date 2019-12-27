'''This datatype is SET'''
s={10,3.5,'abc',10,4.5,'xyz'}
print(s)

s.add(23)
print(s)

s.update(['a','b'])
print(s)

s.pop()
print(s)

s.discard('abc')
print(s)

s.remove(23)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

print(s1|s2)
'''
this 
is union
'''

print(s1&s2)
'''
this is 
intersection
'''

print(s1-s2)
'''this is 
subraction
 from 1st to 2nd
'''
print(s1^s2)
'''this is 
difference between 
both
'''