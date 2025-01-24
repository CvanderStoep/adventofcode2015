from dataclasses import dataclass

@dataclass
class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

# Example instance of the dataclass
ingredient = Ingredient(capacity=0, durability=0, flavor=0, texture=0, calories=0)

# Property name stored in a string variable
property_name = 'flavor'
property_value = 10

# Using setattr to assign a value to the property
setattr(ingredient, property_name, property_value)

# Print the updated dataclass instance
print(ingredient)
