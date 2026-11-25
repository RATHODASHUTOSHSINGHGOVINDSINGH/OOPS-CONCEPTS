#method-overloading / compile time polymorphism in python
#Variable number of arguments
#Example 3
class calculator:
    def add(self, *nums): # * it accepts any number of positional arguments
        return sum(nums) #python function
cal = calculator()
print(cal.add(2,3,4))
print(cal.add(2))
print(cal.add(24,45))