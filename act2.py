from abc import ABC , abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("I can slither on the ground")
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
r = human()
r.move()

r = snake()
r.move()

r = dog()
r.move()

r = lion()
r.move()