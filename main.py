def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        return f.read().strip()


def move_(direction: str, location: tuple[int, int]) -> tuple[int, int]:
    directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    dx, dy = directions[direction]
    return location[0] + dx, location[1] + dy


def compute_locations(moves: str, is_part_two: bool = False) -> int:
    location_santa = location_robo_santa = (0, 0)
    locations = {(0, 0)}

    for idx, move in enumerate(moves):
        if is_part_two and idx % 2 == 1:
            location_robo_santa = move_(move, location_robo_santa)
            locations.add(location_robo_santa)
        else:
            location_santa = move_(move, location_santa)
            locations.add(location_santa)

    return len(locations)


if __name__ == '__main__':
    moves = read_input_file('input/input3.txt')
    print(f"Part I: {compute_locations(moves)}")
    print(f"Part II: {compute_locations(moves, is_part_two=True)}")
