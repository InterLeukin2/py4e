class A:
    def greet(self):
        print("Hello from class A")

class B(A):
    def greet(self):
        print("Hello from class B")

class C(A):
    def greet(self):
        print("Hello from class C")

class D(B, C):
    pass

class E(A, C):
    pass
class M(E,D):

d = M()
d.greet()  # 输出什么？