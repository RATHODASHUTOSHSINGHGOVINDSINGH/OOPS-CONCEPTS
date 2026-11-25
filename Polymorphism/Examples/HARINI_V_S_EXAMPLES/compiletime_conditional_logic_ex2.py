#method-overloading/compile time polymorphism in python
#Variable arguments + Conditional logic
#Example 2
class Calculator:
    def add(self, *nums):
        if len(nums)==2:
            return nums[0] + nums[1] #accesses the first 2 numbers
        elif len(nums)==3:
            return nums[0]+nums[1]+nums[2]
        else:
            return sum(nums)
cal = Calculator()
print(cal.add(10,20))# stored inside method -> nums = (10,20) -> stores as tuple
print(cal.add(10,20,30,40))
print(cal.add(10,20,30))