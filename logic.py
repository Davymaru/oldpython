"""
    Creating and using a Dog SuperClass 🐕
    and a herding dog sub class 🐏🐏🐏

    and instantiating (making objects)
"""


class Dog:
    # dog is a Super class of the Herding_Dog class
    def __init__(self, color, coat, size):
        self.color = color
        self.coat = coat
        self.size = size

    def bark(self):
        print("Woof!")

    def happy(self):
        print("Wag wag")


class HerdingDog(Dog):
    def herding(self):
        print("Go over here! Get me a cookie!")


def main():

    print("\n\n")
    ollie = Dog("Fawn", "Short", "Large")
    print("Ollie: ")
    ollie.bark()
    ollie.happy()

    print("\n\n")
    print("Nessie:")
    nessie = HerdingDog("Black", "Short", "Large")
    nessie.herding()
    print("\n\n")


main()
