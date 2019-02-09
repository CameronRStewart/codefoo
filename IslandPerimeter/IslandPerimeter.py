# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
# You can either copy and paste the Strings into your function call, or look at the input files in the repo.
#
# Example 1
# Input: [
#
# [0,1,0,0],
#
# [1,1,1,0],
#
# [0,1,0,0],
#
# [1,1,0,0]
#
# ]
#
# Output: 16
#
# Explanation: The perimeter is the 16 yellow stripes, seen in this image

# Need a function 'neighbors' that given a coordinate, tells how many neighbors there are.
# Need a simple function 'sides', given isLand bool and neighbors count, returns side count.
# Iterate over each item, check neighbors, get side count.

#Map: squared = list(map(lambda x: x**2, items))
#Reduce: product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

from functools import reduce


class IslandPerimeter:

    def __init__(self, grid):
        self.grid = grid
        self.x_len = len(grid)
        self.y_len = len(grid[0])
        self.perimeter = 0

    def get_perimeter(self):
        # reduce the reduce of the map of sides_count
        total_count = 0
        for x_index, row in enumerate(self.grid):
            total_count += self.row_perimeter_sides(row, x_index)
        return total_count

    def row_perimeter_sides(self, row, x_index):
        count = 0
        for y_index, val in enumerate(row):
            if val == 1:
                sides = self.sides_count(self.count_neighbors((x_index, y_index)))
                count += sides
        return count

    def count_neighbors(self, coord):
        x = coord[0]
        y = coord[1]
        # above: (x-1, y)
        # below: (x+1, y)
        # left:  (x, y-1)
        # right: (x, y+1)
        # All above IF x and y >= 0 and < x size, y size
        # Above
        if (x - 1) >= 0:
            above = self.grid[(x - 1)][y]
        else:
            above = 0
        # Below
        if (x + 1) < self.x_len:
            below = self.grid[(x + 1)][y]
        else:
            below = 0
        # Left
        if (y - 1) >= 0:
            left = self.grid[x][(y - 1)]
        else:
            left = 0
        # Right
        if (y + 1) < self.y_len:
            right = self.grid[x][(y + 1)]
        else:
            right = 0

        return [above, below, left, right]

    def sides_count(self, neighbors):
        perimeter_sides = 0
        for n_count in neighbors:
            perimeter_sides += abs((n_count - 1))
        return perimeter_sides

i = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
ip = IslandPerimeter(i)
print(ip.get_perimeter())
