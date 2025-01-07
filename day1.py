def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content[0]


def compute_part_one(file_name: str) -> int:
    content = read_input_file(file_name)
    go_up = content.count('(')
    go_down = content.count(')')
    destination = go_up - go_down

    return destination


def compute_part_two(file_name: str) -> int:
    content = read_input_file(file_name)
    return "part 2 not yet implemented"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input1.txt')}")
    print(f"Part II: {compute_part_two('input/input1.txt')}")
