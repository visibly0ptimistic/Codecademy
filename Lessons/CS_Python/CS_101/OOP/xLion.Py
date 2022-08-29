# Create your class here
class Lion:
    # Create a __init__ method
    def __init__(self, name, king, age, is_brave, is_cuddly):
        # Create a new pet!
        self.name = name
        self.king = king
        self.age = age
        # Added is_brave
        self.is_brave = is_brave
        self.is_cuddly = is_cuddly

# Create method to change
# at least one attribute.
# Ex: def change_att(self):
    def have_birthday(self):
        self.age = self.age + 1
        print("{name} has a birthday! {name} is {age} years old.".format(name = self.name, age = self.age))

# if the other cat is NOT
# brave, they will be 
# scared
    def scare(self, other_lion):
        if(other_lion.is_brave):
            print("{other_name} was NOT scared of {name}!".format(name = self.name, other_name = other_lion.name))
        else:
            print("{other_name} was scared by {name}!".format(name = self.name, other_name = other_lion.name))
            
# Create a __repr__ method
    def __repr__(self):
    # Printing a Cat will
    # tell you its name, its
    # breed, its age, and
    # if it's cuddly.
        description = "This Lion named {name} is {age} years old.".format(name = self.name, age=self.age)
        if self.is_cuddly:
            description += " {name} is a cuddly cat.".format(name = self.name)
        else:
            description += " {name} is not a cuddly cat.".format(name = self.name)
        return description

# Call your method on your
# new pet here.
new_lion = Lion("James", True, 7, False, True)
new_lion.have_birthday()

new_lioness = Lion("Lia", False, 23, True, True)
new_lioness.have_birthday()

# James is NOT brave and will 
# be scared
new_lioness.scare(new_lion)

# Lia is brave and will 
# NOT be scared
new_lion.scare(new_lioness)

# Print out your pet below!
print(new_lion)