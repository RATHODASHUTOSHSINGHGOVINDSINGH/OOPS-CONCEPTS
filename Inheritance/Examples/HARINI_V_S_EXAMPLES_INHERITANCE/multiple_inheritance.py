#Multiple Inheritance
#Example 1
class Mom:
    def caring(self):
        print("My Mom is a caring person")
class Dad:
    def gentleman(self):
        print("My Dad is a wise man")
class Child(Mom,Dad):
    def responsible(self):
        print("I am a responsible kid")

#Object for Child class
c1 = Child()
c1.gentleman()
c1.caring()
c1.responsible()

#Example 2
class Grandma:
    def __init__(self,gname,gage):
        self.gname = gname
        self.gage = gage

class Grandpa:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Mom(Grandma, Grandpa):
    def __init__(self,mname,mage,name,age,gname,gage):
        self.mname = mname
        self.mage = mage
        Grandma.__init__(self,gname,gage)
        Grandpa.__init__(self,name,age)
    def display(self):
        print("My Grandma's name is ", self.gname)
        print("My Grandma's age is", self.gage)
        print("My Grandpa's name is", self.name)
        print("My Grandpa's age is", self.age)
        print("My Mom's name is", self.mname)
        print("My Mom's age is", self.mage)

#object for Mom(Child) class
M1 = Mom("Laya",59,"Shri Ram",91,"Sita",89)
M1.display()