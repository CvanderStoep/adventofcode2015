import re


def process_instruction(registers: dict, position: int, instruction: str) -> (dict, int):
    pattern = r'-?\d+'
    parts = instruction.replace(',', '').split()

    match parts:
        case ['hlf', reg]:
            registers[reg] //= 2
            position += 1
        case ['tpl', reg]:
            registers[reg] *= 3
            position += 1
        case ['inc', reg]:
            registers[reg] += 1
            position += 1
        case ['jmp', offset]:
            position += int(offset)
        case ['jie', reg, offset]:
            if registers[reg] % 2 == 0:
                position += int(offset)
            else:
                position += 1
        case ['jio', reg, offset]:
            if registers[reg] == 1:
                position += int(offset)
            else:
                position += 1

    return registers, position


# Example usage
registers = {'a': 1, 'b': 0}
position = 0
instruction = "jio a, +2"
registers, position = process_instruction(registers, position, instruction)
print(f"Registers: {registers}, Position: {position}")
