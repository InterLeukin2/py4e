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

class E(D, A):
    pass

#class E(A, D):    这个顺序就会不对
        #pass
#class M(E,D):
   # pass

d = E()
d.greet()  # 输出什么？
print( E.__mro__)

