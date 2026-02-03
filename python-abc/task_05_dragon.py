#!/user/bin/python3
"""
Define class Dragon that extends the built-in iterator
 obtained from the iter function


"""


# Parent class: SwimMixin

class SwimMixin:
    def swim(self):
        print("The creature swims")


# Parent class: FlyMixin

class FlyMixin:
    def fly(self):
        print("The creature flies")

# Child class: Dragon


class Dragon(SwimMixin, FlyMixin):

    def swim(self):
        print("The creature swims!")

    def fly(self):
        print("The creature flies!")

    def roar(self):
        print("The dragon roars!")
