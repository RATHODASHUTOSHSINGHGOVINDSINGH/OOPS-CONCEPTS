#method-overloading/compile time polymorphism in python
#Simple example with add() method
#Example 1
class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
    # def add(self,a,b,c,d): #throws an error
    #     print(a+b+c+d)
    #Exception has occurred: TypeError
    # Calculator.add() missing 2 required positional arguments: 'c' and 'd'
cal = Calculator()
print(cal.add(10,20)) # two arguments
print(cal.add(10,20,30)) # three arguments


