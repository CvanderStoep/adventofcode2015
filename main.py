import numpy as np

# Create a sample 2D array
grid = np.zeros((15,8))

grid[2:5+1, 4:8] = 2


print(grid)