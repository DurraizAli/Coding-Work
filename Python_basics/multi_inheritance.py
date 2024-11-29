class A:
    def method(self):
        print("Method from A")

class B:
    def b_method(self):
        print("Method from B")

class C(A,B):
    def hello():
        pass

my_multi = C()
my_multi.method()
my_multi.b_method()