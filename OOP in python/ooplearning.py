class car:
    def drive(self):
        print("the car is driving")
my_car = car()
my_car.drive()


class person:
    def __init__(self,name,age):
        self.name= name
        self.age=age
    def greet(self):
        print(f"Hello,my name is {self.name} and i am {self.age} years old.")

person1=person("hamza",20)
person1.greet()



class bag:
    def __init__(self,bag1,bag2):
        self.bag1 = bag1
        self.bag2 = bag2
    def better(self):
        print(f"The {self.bag1} is better than {self.bag2}")
        


my_bag =  bag("leather bag","clothe bag")
my_bag.better()


# using inheritance (class in class)
class dog:
    def bark(self):
        print("Dogs do woof!")
class cat(dog):
    def speaks(self):
        print("cats do meow")
d = cat()
d.speaks()
d.bark()


# using inheritance,encapsulation,polymorphism
# making a mini project for better understanding

class person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def details(self):
        print(f"Name:{self.name} ,Age:{self.age} ,ID:{self.id}")
    def intro(self):
        print("i am a person")

class student(person):
    def __init__(self, name, age, id,grade):
        super().__init__(name, age, id)
        self.grade = grade
    def intro(self):
        print(f"I am a student of grade {self.grade} and my name is {self.name}")
        
class teacher(person):
    def __init__(self, name, age, id,subject):
        super().__init__(name, age, id)
        self.subject = subject
    def intro (self):
        print(f"i am a teacher ,my name is {self.name} and my subject is {self.subject}.")

s1 = student("hamza",22,10581,13)
t1 = teacher("ahsan",22,2314,"python")

s1.details()
s1.intro()
 
t1.details()
t1.intro()
