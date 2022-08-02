class A:
    def __init__(self, a, b):
        print("This is a constructor")
        c = a + b

    def hello(self):
        print("Hello world")

    def sum(self,c):
        print("Sum from Contructor = " + str(c))


obj = A(34, 16)
obj.hello()


