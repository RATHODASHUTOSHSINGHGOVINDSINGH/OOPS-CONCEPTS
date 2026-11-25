#method-overloading / compile time polymorphism in python
#Default arguments
#Example 4

class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
    # def add(self,a,b,c,d):
    #     print(a+b+c+d)
cal = Calculator()
print(cal.add(10,20)) # two arguments
print(cal.add(10,20,30))