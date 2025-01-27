from collections import defaultdict
import sympy

def compute_part_two(file_name: str) -> int:
    required_presents = read_input_file(file_name)
    print(required_presents)

    elf_visits = defaultdict(int)
    house = 1

    while True:
        divisors = sympy.divisors(house)
        presents = 0
        for elf in divisors:
            if elf_visits[elf] < 50:
                elf_visits[elf] += 1
                presents += elf * 11

        if house % 100000 == 0:
            print(house, presents)

        if presents >= required_presents:
            print(f'house= {house}')
            break

        house += 1

# Example usage
file_name = "input.txt"
compute_part_two(file_name)
