class A:
    def parent1(self):
        print("I am parent method 1 ")

class B:
    def parent2(self):
        print("I am parent method 2")

class C(A,B):
    def child(self):
        print("I am child method")


c1 = C()
c1.parent1()
c1.parent2()
c1.child()