class Test:
    def __init__(self,n):
        self.num = n
        
    def __str__(self):
        return "{}".format(self.num)
    
    def __add__(self, other):
        return self.num+other.num
        
    def __sub__(self, other):
        return self.num-other.num
    
    def __lt__(self, other):
        return self.num<other.num
        
t1 = Test(10)
print(t1)

t2 = Test(7)
print(t2)

print(t1+t2)
print(t1-t2)
print(t1<t2)
