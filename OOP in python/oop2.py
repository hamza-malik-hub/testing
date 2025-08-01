class car:
    def __init__(self,driving):
     self.driving = driving
    def __str__(self):
       return f"can you drive?:{self.driving}"

d = car("Yes I can drive.")
print(d)


class classroom:
   def __init__(self,students):
      self.students = students
   def __len__(self):
      return len(self.students)
c= classroom(["hamza","usman","ahsan","faizan"])
print (len(c))


class fruits:
   def __init__(self,items):
      self.items=items
   def __add__(self,veg):
      return fruits(self.items + veg.items)
f = fruits(["banana","mango"])
v = fruits(["cucumber"])
whole = f + v
print (whole.items)


class colors:
   def __init__(self,colours):
      self.colours = colours
   def __eq__(self,others):
      
      return self.colours==others.colours

color1 = colors("blue")
color2 = colors("black")
color3 = colors("blue")

print(color1==color2)
print(color1==color3)


from abc import ABC
class animals(ABC):
   def sounds(self):
      pass

class dogs(animals):
   def sounds(self):
      return "bark" 

class cats(animals):
   def sounds(self):
      return "meow"

d= dogs()
print(d.sounds())             

from abc import ABC 
class  instruments(ABC):

   def play_sound(self):
      pass

class drum(instruments):
   def play_sound(self):
      return "BOOM BOOM"
   
class guitar(instruments):
   def play_sound(self):
      return "tring tring"
   
d = drum()
g = guitar()
for instrument in [ g , d]:
   print(instrument.play_sound())
