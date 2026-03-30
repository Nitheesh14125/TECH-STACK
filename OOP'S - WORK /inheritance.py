class parent:
    def parent_method(self):
        print("I am from parent class method i can called from parent class object and child class object if i called from child class that concept is called as inheritance")
    
class child(parent):
    def child_method(self):
        print("I am from child class method")



c = child()
c.parent_method()
c.child_method()