class MyClass:

    def __init__(self,value):
        self.val = value


    def show(self):
        print(f"Value is {self.val}")


    @property                   #getter
    def ten_value(self):
        return 10 * self.val


    @ten_value.setter
    def ten_value(self, new_value):
        self.val = new_value/10



obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()