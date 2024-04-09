
def main():

    class Pet:
        vet_name = "Your Veterinary Office"

        def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
            self.__owner_first_name = owner_first_name

            self.__owner_last_name = owner_last_name

            self.__pet_id = pet_id

            self.__pet_name = pet_name

            self.__pet_type = pet_type


        def get_owner_first_name(self):
            return self.__owner_first_name

        def get_owner_last_name(self):
            return self.__owner_last_name

        def get_pet_id(self):
            return self.__pet_id

        def get_pet_name(self):
            return self.__pet_name

        def get_pet_type(self):
            return self.__pet_type


        def set_owner_first_name(self, owner_first_name):
            self.__owner_first_name = owner_first_name

        def set_owner_last_name(self, owner_last_name):
            self.__owner_last_name = owner_last_name

        def set_pet_id(self, pet_id):
            self.__pet_id = pet_id

        def set_pet_name(self, pet_name):
            self.__pet_name = pet_name

        def set_pet_type(self, pet_type):
            self.__pet_type = pet_type

        def display_pet_info(self):
            print("Pet Information:")

            print("Owner: {} {}".format(self.__owner_first_name, self.__owner_last_name))

            print("Pet ID:", self.__pet_id)

            print("Pet Name:", self.__pet_name)

            print("Pet Type:", self.__pet_type)

            print("Veterinary Office:", Pet.vet_name)

            print()


    def check_property(pet, property_name):
        if hasattr(pet, property_name):
            print(f"The property '{property_name}' exists for the pet.")
        else:
            print(f"The property '{property_name}' does not exist for the pet.")


    pet1 = Pet("Runnout", "Ideas", 1, "Foname")

    pet2 = Pet("Pieron", "Kelley", 2, "Thunder", "Cat") #my real cats name fun fact

    pet3 = Pet("Sephiroth", "One winged angel", 3, "cloud")


    pet1.set_pet_type("Snake")


    pet1.display_pet_info()

    pet2.display_pet_info()

    pet3.display_pet_info()


    print("Property Existence Check:")

    check_property(pet1, "get_pet_type")

    check_property(pet2, "get_pet_type")

    check_property(pet3, "get_owner_last_name")

    check_property(pet3, "get_pet_age")






main()
