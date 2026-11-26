#public
class Student:
    name="janvi"
 
obj = Student()
print(obj.name)

#protected
class Student:
    _marks = 90
    
obj = Student()
print(obj._marks)
 
 
 #protected
class Student:
  _marks = 90
    
obj= Student()
print(obj._marks)


#all three in one example.

class Student:
    def __init__(self):
        self.name="janvi" #public
        self._marks =90 #protected
        self.__age =21 #private
        
    def display(self):
        print(self.name)
        print(self._marks)
        print(self.__age)
        
Student().display()


#getter example
class Student:
    def __init__(self):
        self.__marks =90
        
    def get_marks(self):
        return self.__marks
    
obj = Student()
print(obj.get_marks())

#setter example
class Student:
    def __init__(self):
        self.__marks = 90
        
    def set_marks(self,marks):
        self.__marks = marks
        
    def display(self):
        print(self.__marks)
        
obj = Student()
obj.set_marks(95)
obj.display()