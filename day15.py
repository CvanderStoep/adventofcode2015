# z3 solver, pip install z3-solver
# dataclass
# optimize, constraints

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
    teaspoons = [Int(f'ts{i}') for i in range(0, n)]
    # print(teaspoons)
    for ts in teaspoons:
        s.add(ts >= 0)
        # s.add(ts <= 100)
    s.add(sum(teaspoons) == 100)

    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    # capacity = sum(teaspoons[i] * ingredients[i].capacity for i in range(n))
    # durability = sum(teaspoons[i] * ingredients[i].durability for i in range(n))
    # flavor = sum(teaspoons[i] * ingredients[i].flavor for i in range(n))
    # texture = sum(teaspoons[i] * ingredients[i].texture for i in range(n))

    for i in range(n):
        capacity += teaspoons[i] * ingredients[i].capacity
        durability += teaspoons[i] * ingredients[i].durability
        flavor += teaspoons[i] * ingredients[i].flavor
        texture += teaspoons[i] * ingredients[i].texture
        calories += teaspoons[i] * ingredients[i].calories

    if part == 2:
        s.add(calories == 500)

    capacity = If(capacity < 0, 0, capacity)
    durability = If(durability < 0, 0, durability)
    flavor = If(flavor < 0, 0, flavor)
    texture = If(texture < 0, 0, texture)

    objective = capacity * durability * flavor * texture

    # print(objective)
    optimize = Optimize()
    optimize.add(s.assertions())
    optimize.maximize(objective)

    # print(s)
    if optimize.check() == sat:
        model = optimize.model()
        # print(model)
        max_value = model.evaluate(objective)
        capacity_value = model.evaluate(capacity)
        print(f"Maximum value: {max_value}")
        # print(f"Capacity value: {capacity_value}")
        for v in teaspoons:
            print(f"{v} = {model.evaluate(v)}")
    else:
        print("No solution found")

    return max_value


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input15.txt', part=1)}")
    print(f"Part II: {compute_part('input/input15.txt', part=2)}")
