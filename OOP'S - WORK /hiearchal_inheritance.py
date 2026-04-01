class A:
    def parent(self):
        print("Parent method")

class B(A):
    def child1(self):
        print("Child method1")

class C(A):
    def child2(self):
        print("child method2")


c1 = C()
c1.child2()
c1.parent()


c2 = B()
c2.child1()
c2.parent()