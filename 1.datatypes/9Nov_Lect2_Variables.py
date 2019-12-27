Lecture 2 : Pass by reference, Pass by value is available in Python

a=b=c=10
p,q,r=1,2,3

print(a,b,c)
print(p,q,r)

Data Structure : To assign multiple values in a variable
1. List : Collection of heterogenous data 
Definition : l=[10,2.3,'abc',True.[1,2,3]]
* A list can contain list within itself
*List also have the sequence of characters stored at index
*List are mutables: values of list can be amended/changed at the given index of the list
*Content of list has to be defined within "[]" square brackets.
*Multiple values can be amended/changes within a list using concept of 'Slicing' eg: l[1:3],
this concept works by (n-1), i.e above will return the values placed at index 1,2 of list.

l = [1,'abc',[10,20,30]]


2.Tuple : Collection of heterogenous data
Definition : t=(12,3.4,[10,2,3],(9,43,5))
*Tuples are immutable(elements/values within tuple can't be changed) with an exception of list within tuple which can be amended
*Packing of tuple : Assigning multiple variable to a variable is by default considered as tuple
a= 10,20,30 #Packing of tuple
print(a)
x,y,z = a #Unpacking of tuple
print(x,y,z)


3.Set : Collection of unique heterogenous elements/values without index
Definition :s={10,a,r}
*Values of set can't be accessed by using index.
*List and tuple can be inserted within Set.


4.Dictionary:
*index = key , values are defined in key value pair.
Keys are user defined indices where values are stored.
*Key can't be repeated within dictionary
*Values can be accessed and updated using the key of dictionary.
*Define string ket using quotes and number key has to be defined without quotes

OPERATORS :
1.Assignment : used to assign a value to variable , right to left.
2.Arithmeric Operator : +,-,*, "true division" /,"floor division" //,"exponent" **.
*Combination of assignment and arithmetic perators can be used eg : a+=5 ( a=a+5), a-= 5 (a=a-5)
eg: increment operator can be defined as a+=1 (a++) , a-=1(a--),there is no concept of increment operators(a++ and a--)in python.
3.Comparison operator: <,>,<=,>=,==,!=.
4.Logical operator : and , or .eg : print(True and True), print(True or False)
*Output of Logical and comparison operator will always be boolean.
5.Identity operator : is , is not eg:
a=10
b=10
print(a is b)
o/p= True 
however two distinct lists with same contents will return False for this identity comparison

6: Membership operator :in , not in
eg : str =("Howdie Chaps")
print("H" in str)
o/p =True
print("Z" in str)
o/p = false

With exception of dictionary where  Membership operator checks for Key and not the values. to access the values <dictionary names>.values() can be used.
