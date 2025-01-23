import re
from z3 import *
from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    ingredients = []
    pattern = r'-?\d+'  # pattern for positive and negative integers
    for line in content:
        parts = line.split()
        name = parts[0][:-1]
        parts = re.findall(pattern, line)
        capacity = int(parts[0])
        durability = int(parts[1])
        flavor = int(parts[2])
        texture = int(parts[3])
        calories = int(parts[4])

        ingredient = Ingredient(name, capacity, durability, flavor, texture, calories)
        ingredients.append(ingredient)

    return ingredients


def compute_part(file_name: str, part=1) -> int:
    ingredients = read_input_file(file_name)
    print(ingredients)

    n = len(ingredients)
    s = Solver()

    teaspoons = [Int(f'ts{i}') for i in range(n)]
    for ts in teaspoons:
        s.add(ts >= 0)
    s.add(sum(teaspoons) == 100)

    # Initialize properties to zero
    capacity = durability = flavor = texture = calories = 0

    # Cache for computed values to avoid redundant calculations
    computed_cache = {}

    def get_property_value(teaspoons, property_name):
        # Create a tuple key for the cache
        cache_key = (tuple(teaspoons), property_name)
        if cache_key in computed_cache:
            return computed_cache[cache_key]

        # Compute property value if not in cache
        value = sum(teaspoons[i] * getattr(ingredients[i], property_name) for i in range(n))
        computed_cache[cache_key] = value
        return value

    # Compute total properties using the cache
    capacity = get_property_value(teaspoons, 'capacity')
    durability = get_property_value(teaspoons, 'durability')
    flavor = get_property_value(teaspoons, 'flavor')
    texture = get_property_value(teaspoons, 'texture')
    calories = get_property_value(teaspoons, 'calories')

    if part == 2:
        s.add(calories == 500)

    capacity = If(capacity < 0, 0, capacity)
    durability = If(durability < 0, 0, durability)
    flavor = If(flavor < 0, 0, flavor)
    texture = If(texture < 0, 0, texture)

    objective = capacity * durability * flavor * texture

    optimize = Optimize()
    optimize.add(s.assertions())
    optimize.maximize(objective)

    if optimize.check() == sat:
        model = optimize.model()
        max_value = model.evaluate(objective)
        print(f"Maximum value: {max_value}")
        for v in teaspoons:
            print(f"{v} = {model.evaluate(v)}")
    else:
        print("No solution found")

    return max_value

if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input15.txt', part=1)}")
    print(f"Part II: {compute_part('input/input15.txt', part=2)}")
