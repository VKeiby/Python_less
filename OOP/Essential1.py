class MyObject:
    class_attr = 8

    def __init__(self):
        self.data_attr = 42

    def instance_method(self):
        print(self.data_attr)

    @staticmethod
    def static_method():
        print(MyObject.class_attr)

if __name__ == '__main__':
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()