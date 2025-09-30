from lib.helpers import check_that_these_are_equal

# So far we've seen lists that contain single values. But lists can contain
# other lists too! These are called 2D lists (or two-dimensional lists).

# Think of a 2D list like a grid or a table. Here's an example:

grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# This represents a 3x3 grid that looks like:
# 1 2 3
# 4 5 6
# 7 8 9

# To access an element in a 2D list, we use two indices:
# The first index selects the row (which list)
# The second index selects the column (which element in that list)

print("The element at row 0, column 0 is:")
print(grid[0][0])  # This prints 1

print("The element at row 1, column 2 is:")
print(grid[1][2])  # This prints 6

# @TASK: Print the element at row 2, column 1 (should be 8)
print("The element at row 2, column 1 is:")
# Your code here

# We can also modify elements in a 2D list:
grid[1][1] = 99
print("After changing the centre element:")
print(grid)

# == Looping through 2D lists ==

# To visit every element in a 2D list, we need nested loops:

print("\nAll elements in the grid:")
for row in grid:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row

# We can also use indices if we need to know the position:

print("\nElements with their positions:")
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(f"grid[{i}][{j}] = {grid[i][j]}")

# == Creating 2D lists ==

# We can create a 2D list filled with zeros like this:
rows = 3
cols = 4
zeros = [[0 for j in range(cols)] for i in range(rows)]

print("\n3x4 grid of zeros:")
for row in zeros:
    print(row)

# @TASK: Create a 2x2 identity matrix (1s on diagonal, 0s elsewhere)
# It should look like:
# [[1, 0],
#  [0, 1]]

def create_identity_matrix(size):
    # Your code here
    pass

check_that_these_are_equal(
    create_identity_matrix(2),
    [[1, 0], [0, 1]]
)

check_that_these_are_equal(
    create_identity_matrix(3),
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
)

# == Real world example: Tic-Tac-Toe board ==

# 2D lists are perfect for game boards!

tic_tac_toe = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    [' ', ' ', 'X']
]

# @TASK: Write a function that checks if 'X' won by getting three in a row
# (just check horizontal rows for now)

def check_x_wins_horizontally(board):
    # Your code here
    pass

check_that_these_are_equal(
    check_x_wins_horizontally([
        ['X', 'X', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ]),
    True
)

check_that_these_are_equal(
    check_x_wins_horizontally([
        ['X', 'O', 'X'],
        ['O', 'O', 'O'],
        ['X', 'X', ' ']
    ]),
    False
)

# When you're done, move on to 031_oop.py