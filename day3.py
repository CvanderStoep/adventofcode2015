def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content[0]


def compute_part_one(file_name: str) -> int:
    directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}

    moves = read_input_file(file_name)
    location = (0, 0)
    locations = set()
    locations.add(location)

    for move in moves:
        x, y = location
        dx, dy = directions[move]
        location = x + dx, y + dy
        locations.add(location)

    number_of_visited_houses = len(locations)

    return number_of_visited_houses


def compute_part_two(file_name: str) -> int:
    content = read_input_file(file_name)
    return "part 2 not yet implemented"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input3.txt')}")
    print(f"Part II: {compute_part_two('input/input3.txt')}")
