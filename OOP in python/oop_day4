class Dog:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"dog:({self.name})"
dog = Dog("rex")

print (repr(dog))
print([dog])

import gc
class cat:
    def __init__(self,name):
        self.name = name
        print( f"{self.name} is created.")
    def __del__(self):
        return f"{self.name} is destroyed."
    
c = cat("meow")
del c

gc.collect()



class Mylist:
    def __init__ (self,item):
        self.item = item
    def __getitem__(self,index):
        return self.item[index]
Item = Mylist(["apple","mango","banana"])
print(Item[2])
print(Item[0])
print(Item[1])

