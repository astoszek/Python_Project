class MyClass:
    def __init__(self, y=23):
        self.x = 1
        self.y = y


obj = MyClass
obj.my_method(1)
obj.my_method("A")
obj.my_method(True)
