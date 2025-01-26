def get_grid(grid, i, j):
    # Assume this function returns the value at grid[i][j] if within bounds, else returns "."
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return grid[i][j]
    return "."

def update_cell(grid, i, j):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    number_on_neighbours = 0

    for direction in directions:
        di, dj = direction
        if get_grid(grid, i + di, j + dj) == "#":
            number_on_neighbours += 1

    if get_grid(grid, i, j) == "#":
        if 2 <= number_on_neighbours <= 3:
            light = "#"
        else:
            light = "."
    else:
        if number_on_neighbours == 3:
            light = "#"
        else:
            light = '.'

    return light

def update_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[0])):
            new_row.append(update_cell(grid, i, j))
        new_grid.append(new_row)
    return new_grid

# Example usage
grid = [
    [".", "#", "."],
    ["#", "#", "#"],
    [".", "#", "."]
]

# Update the grid
new_grid = update_grid(grid)

# Print the updated grid
for row in new_grid:
    print("".join(row))
