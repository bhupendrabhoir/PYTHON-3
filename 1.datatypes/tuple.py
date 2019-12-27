'''This datatype is Tuple'''
t=(10,3.5,'abd',[1,2,3],'xyz')
print(t)
print(t[1])
print(t[3][1])
t[3][2]=999
print(t)

del t
t.clear()


print(('a','b','c')+(1,2,3,4,5))

tup=(10,5,33,21,30)

print(t.index('xyz'))
print(t.count('xyz'))