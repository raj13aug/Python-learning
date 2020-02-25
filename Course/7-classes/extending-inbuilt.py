class Test(str):
    def duplicate(self):
        return self + self

text = Test("Python")
print(text.duplicate())


text = Test("Python")
print(text.lower())

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append(1)
