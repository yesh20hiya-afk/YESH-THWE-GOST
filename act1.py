from abc import ABC , abstractmethod

class ABsclass:
    def print(self,x):
        print("past value:", x)
    @abstractmethod
    def task(self):
        print("we are inside abcsclass")
class testclass(ABsclass):
    def task(self):
        print("we are inside testclass")
test_object= testclass()
test_object.task()
test_object.print(100)
        
    



