class Student:
    def __init__(self):
        self._name = "Rishi"
        
        
    def _fullname(self): #protected method
        
        return "CodewithRishi"
    
    
class Subject(Student): #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj)) 

#calling by object of Student class
print(obj._name)
print(obj._fullname()) 
#calling by object of Student class
print(obj1._name)
print(obj1._fullname()) 



     