class fct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compt(self):
        return self.x + self.y


class form(fct):
    pass


body = fct(1, 2)
c = body.compt()
print(c)
