def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content[0]


def process_sequence(sequence: str) -> str:
    position = 0
    new_sequence = ''
    l = len(sequence)
    while position < l:
        count = 1
        while (position + count) < l and sequence[position] == sequence[position + count]:
            count += 1
        new_sequence += str(count)
        new_sequence += sequence[position]
        position += count

    return new_sequence


def compute_part(file_name: str, number_of_sequences=40) -> int:
    sequence = read_input_file(file_name)
    print(sequence)
    for _ in range(number_of_sequences):
        sequence = process_sequence(sequence)
    print(f'{len(sequence)= }')

    return len(sequence)


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input10.txt', 40)}")
    print(f"Part II: {compute_part('input/input10.txt', 50)}")
