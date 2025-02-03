import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def process_instruction(a: int, b: int, position: int, instruction: str) -> (int, int, int):
    pattern = r'-?\d+'
    if 'hlf' in instruction:
        if instruction[-1] == 'a':
            a = a // 2
        else:
            b = b // 2
        position += 1
    if 'tpl' in instruction:
        if instruction[-1] == 'a':
            a = a * 3
        else:
            b = b * 3
        position += 1
    if 'inc' in instruction:
        if instruction[-1] == 'a':
            a += 1
        else:
            b += 1
        position += 1
    if 'jmp' in instruction:
        jump = int(re.findall(pattern, instruction)[0])
        position += jump
    if 'jie' in instruction:
        if instruction[4] == 'a':
            r = a
        else:
            r = b
        if r % 2 == 0:
            jump = int(re.findall(pattern, instruction)[0])
            position += jump
        else:
            position += 1
    if 'jio' in instruction:
        if instruction[4] == 'a':
            r = a
        else:
            r = b
        if r == 1:
            jump = int(re.findall(pattern, instruction)[0])
            position += jump
        else:
            position += 1

    return a, b, position


def compute_part_one(file_name: str) -> int:
    instructions = read_input_file(file_name)
    print(instructions)
    a, b, position = 0, 0, 0

    while position < len(instructions):
        instruction = instructions[position]
        a, b, position = process_instruction(a, b, position, instruction)

    return b


def compute_part_two(file_name: str) -> int:
    instructions = read_input_file(file_name)
    a, b, position = 1, 0, 0

    while position < len(instructions):
        instruction = instructions[position]
        a, b, position = process_instruction(a, b, position, instruction)

    return b


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input23.txt')}")
    print(f"Part II: {compute_part_two('input/input23.txt')}")
