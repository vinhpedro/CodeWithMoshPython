from abc import ABC, abstractclassmethod


class UIControl:
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Textbox")


class DropDownList(UIControl):
    def draw(self):
        print("DropdownList")


def draw(controls):
    for control in controls:
        control.draw()


text = TextBox()
drop = DropDownList()

draw([text, drop])
