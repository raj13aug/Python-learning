from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TestBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()

textbox = TestBox()
draw([ddl, textbox])

# Poly Morphism

# many  forms

# In this example, our draw method is taking many different forms, and this is the determined at run time
