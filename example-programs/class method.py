class Hello:
    def __init__(self, var):
        print("Variable value:", var)
    @classmethod
    def zero(cls):
        cls(10)


var1 = Hello.zero()



