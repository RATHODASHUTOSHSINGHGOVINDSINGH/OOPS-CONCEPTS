class A:
    def show(self):
        print("Method from A")


class B(A):
    def show(self):
        print("Method from B")


class C(A):
    def show(self):
        print("Method from C")


class D(C,B):
    pass


obj = D()
obj.show()

print(D.mro())