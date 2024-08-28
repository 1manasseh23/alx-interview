#!/usr/bin/python3


def island_perimeter(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # If there's land on the left, subtract 1 from the perimeter
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

                # If there's land above, subtract 1 from the perimeter
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
