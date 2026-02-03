#!/user/bin/python3
"""
Define class FlyingFish that extends the built-in iterator
 obtained from the iter function


"""


# Parent class: Fish

class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


# Parent class: Birth

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


# Child class: FlyingFish

class FlyingFish(Fish, Bird):

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
