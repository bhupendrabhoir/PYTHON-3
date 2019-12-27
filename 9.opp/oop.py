'''OOP'''
'''eg.
class 1st letter should be capitalize'''
class Person:
    count=0
    def __init__(self,n,h,l):
        self.name=n
        self.hands=h
        self.legs=l
        self.__lp=10
        Person.count+=1
        print("{} is born".format(self.name))
    
    def __del__(self):
        Person.count-=1
        print("{} is died".format(self.name))
    
    def __str___(self):
        return "{} is having {} hands and {} legs".format(self.name, self.hands, self.legs)
        
    def run(self):
        print("{} is running with {} legs".format(self.name, self.legs))
        
    def dotest(self):
        print("Lungpower of {} is {}".format(self.name, self.__lp))

    def doyoga(self):
        self.__lp +=2
        return self.__lp
        
    def smoke(self):
        self.__lp -=1
        return self.__lp
        
    def getcount():
        print("Total count is {}".format(Person.count))
        
    
hari=Person("hariprasad",2,2)
print(hari.name)
print(hari.hands)
print(hari.legs)
hari.name="harry"
hari.run()
print(hari)
hari.__lp=100
hari.dotest()
hari.doyoga()
hari.smoke()
hari.dotest()
del hari

alex=Person("Alexander",2,1)
alex.run()
print(alex)
alex.dotest()
alex.doyoga()
alex.smoke()
alex.smoke()
alex.smoke()
alex.dotest()
Person.getcount()

    