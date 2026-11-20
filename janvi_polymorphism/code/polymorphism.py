class calculator :
    def add(self,a,b=0,c=0):
        return a+b+c


obj = calculator()
print(obj.add(5,3))
print(obj.add(5,3,2))



class number:
    def __init__(self,value):
        self.value = value
        
    def __add__(self,other):
        return self.value + other.value
a=number(10)
b=number(20)
print(a+b)


class animal:
    def sound(self):
        print("animal makes a sound")

class dog(animal):
        def sound(self):
            print("dog bark")
class cat(animal):
        def sound(self):
            print("cat mewos")

dog().sound()
cat().sound()
