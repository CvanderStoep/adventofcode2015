import re
import numpy as np


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_instruction(instruction: str, light_grid) -> None:
    pattern = r'\d+'
    xb, yb, xe, ye = map(int, re.findall(pattern, instruction))

    if instruction.startswith('turn on'):
        light_grid[xb: xe + 1, yb: ye + 1] = 1
    if instruction.startswith('turn off'):
        light_grid[xb: xe + 1, yb: ye + 1] = 0

    if instruction.startswith('toggle'):
        light_grid[xb: xe + 1, yb: ye + 1] = 1 - light_grid[xb: xe + 1, yb: ye + 1]


def process_instruction_two(instruction: str, light_grid) -> None:
    pattern = r'\d+'
    xb, yb, xe, ye = map(int, re.findall(pattern, instruction))

    if instruction.startswith('turn on'):
        light_grid[xb: xe + 1, yb: ye + 1] += 1

    if instruction.startswith('turn off'):
        light_grid[xb: xe + 1, yb: ye + 1] = np.maximum(0, light_grid[xb: xe + 1, yb: ye + 1] - 1)

    if instruction.startswith('toggle'):
        light_grid[xb: xe + 1, yb: ye + 1] += 2


def compute_part(file_name: str, function) -> int:
    # function call to either process_instruction() or process_instruction_two()
    light_grid = np.zeros((1000, 1000))
    instructions = read_input_file(file_name)
    for instruction in instructions:
        function(instruction, light_grid)

    return int(np.sum(light_grid))


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input6.txt', process_instruction)}")
    print(f"Part II: {compute_part('input/input6.txt', process_instruction_two)}")
