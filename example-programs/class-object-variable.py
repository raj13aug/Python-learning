class ABC():
    class_var = 0
    def __init__(self, var):
        ABC.class_var += 1
        self.var = var #object variable
        print("The object value is :", var)
        print("The value of class variable is:", ABC.class_var)

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)