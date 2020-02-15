class ABC():
    def __init__(self, val):  # __init__ method used to initialize the variable of class object.
        print("In class method .....")
        self.val = val
        print("The value is : ", val)

obj = ABC(10)
obj = ABC("Hello")
