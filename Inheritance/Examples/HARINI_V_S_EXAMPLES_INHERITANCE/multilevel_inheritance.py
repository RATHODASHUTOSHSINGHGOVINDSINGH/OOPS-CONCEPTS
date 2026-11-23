#Multilevel Inheritance
#Example 1
class Grandpa:
    def elder(self):
        print("My grandpa is the eldest member of the family")

class Dad(Grandpa):
    def dicipline(self):
        print("My dad is a very organised person")

class Son(Dad):
    def playful(self):
        print("I am happy when I play")

S1 = Son()
S1.elder()
S1.dicipline()
S1.playful()


#Example 2
class Grandma:
    def __init__(self,gname,gage):
        self.gname = gname
        self.gage = gage

class Mom(Grandma):
    def __init__(self,name,age,gname,gage):
        self.name = name
        self.age = age
        Grandma.__init__(self,gname,gage)
class Daughter(Mom):
    def __init__(self,dname,dage,name,age,gname,gage):
        self.dname = dname
        self.dage = dage
        Mom.__init__(self,name,age,gname,gage)
    def display(self):
        print("My Grandma name is ", self.gname)
        print("My Grandma age is", self.gage)
        print("My Mom name is", self.name)
        print("My Mom age is", self.age)
        print("My name is", self.dname)
        print("My age is", self.dage)

D1 = Daughter("Laya",22,"Radha",60,"Sita",89)
D1.display()