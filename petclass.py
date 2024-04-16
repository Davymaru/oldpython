
def main():

    class Pet:

        def __init__(self, kind, breed, name):

            self._kind = kind

            self._breed = breed

            self._name = name
    
        def get_kind(self):

            return self._kind
    
        def set_kind(self, kind):

            self._kind = kind
    
        def get_breed(self):

            return self._breed
    
        def set_breed(self, breed):

            self._breed = breed
    
        def get_name(self):

            return self._name
    
        def set_name(self, name):

            self._name = name
    
        def print_details(self):

            print(f"Pet Details:\nKind: {self._kind}\nBreed: {self._breed}\nName: {self._name}")


    pet1 = Pet("Dog", "husky", "wolfers")

    pet2 = Pet("Cat", "Siamese", "subaru")

    pet3 = Pet("snake", "anaconda", "floobertin")


    pet1.print_details()

    pet2.print_details()

    pet3.print_details()


    print("special method/function:")


    print("Class Name:", Pet.__name__)


main()

