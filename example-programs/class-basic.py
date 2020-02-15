class ABC:
    var = 10  # class variable
    def display(self):
        print("In class method ...")

obj = ABC()      # object
print(obj.var)
obj.display()
