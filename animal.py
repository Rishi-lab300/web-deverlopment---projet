class animal:
    def __init__(self , name , species):
        self.name= name
        self.species = species
          
    def make_sound(self):
        print("Sound made by animal") 
        
            
class Cat(animal): #child class ase banate hemnm
    def __init__(self , name , breed):#child class
        animal.__init__(self, name, species = "Cat")
        self.breed = breed
        self.species1 = 0
          
    def make_sound(self):
        print("Meowwwwww...")   

class Dog(Cat): #child ki child class ase banate hemnm
    def __init__(self , name , breed):#child class
        Cat.__init__(self, name , breed )
        self.breed = breed
          
    def make_sound(self):
        print("bhau bhau bhau")   
        
        
c = Cat("Cato" , "persian") 
c.make_sound()
c = Dog("Dog" , "bulldog") 
c.make_sound()
c = animal("Cat" , "meee")
c.make_sound()
        
        