class Pet:
    
    all = []

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")


        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name} type={self.pet_type} owner={self.owner.name if self.owner else 'None'}>"

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")

        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)