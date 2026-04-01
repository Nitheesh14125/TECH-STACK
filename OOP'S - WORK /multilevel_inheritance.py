class A:
    def grandparent(self):
        print("I am grandparent method")

class B(A):
    def parent(self):
        print("I am parent method")

class C(B):
    def child(self):
        print("I am child method")


c1 = C()
c1.grandparent()
c1.parent()
c1.child()