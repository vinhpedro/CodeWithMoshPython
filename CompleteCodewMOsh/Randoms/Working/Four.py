class Text(str):
    def duplicate(self):
        return self+self


black = "something"
text = Text(black)
text.duplicate()
print(text.duplicate())


class Trackable(list):
    def append(self, object):
        print("Done")
        super().append(object)


list = Trackable()
list.append(1)
