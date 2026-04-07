#if it look like a duck and behave like a duck then it is a duck 

class dog:
    def speak(self):
        print("Bark")

class cat:
    def speak(self):
        print("Meow")
    
def make_sound(animal):
    animal.speak()


d = dog()
c = cat()

make_sound(d)
make_sound(c)