'''
YG  BR  YC  GR  RB
BY  CB  BG  RB  BM
MY  BB  RR  YY  MB
MG  YR  CM  RG  MC
CB  MM  YY  GM  GG
'''

# Read file and represent it in a 5x5 grid

with open("./Testvektoren/tastenfeld5.puzzle", "r") as file:
    matrix = []
    rows, cols = 0, 0
    cell_count = 0
    row = []

    for line in file:
        key = []
        key.append(cell_count)
        key.append(line[0])
        key.append(line[1])

        # Do I really need this?
        key.append(cols)
        key.append(rows)
        row.append(key)
        rows += 1
        cell_count += 1

        if rows == 5:
            cols += 1
            rows = 0
            matrix.append(row)
            row = []

# for line in matrix:
    # print(line)

steps = [0]
history = [matrix[0][0]]
current_square = matrix[0][0]
goal = matrix[4][4]

# Validate next step

def valid(x, y):
    # check if we haven't been here before:
    if matrix[x][y][0] in steps:
        return False;

    # check if next step haas an equal letter in the same position:
    fl = current_square[1] # fl == first letter
    sl = current_square[2] # sl == second letter

    if (fl == matrix[x][y][1]) or (sl == matrix[x][y][2]):
        return True
    
    return False

# Find the next step

def next_step(row, col):

    global current_square

    for x in range (5):
        if not matrix[x][col] == current_square:
            if valid(matrix[x][col][3], matrix[x][col][4]):
                current_square = matrix[x][col]
                steps.append(current_square[0])
                history.append(current_square)
                return current_square

    for y in range (5):
        if not matrix[row][y] == current_square:
            if valid(matrix[row][y][3], matrix[row][y][4]):
                current_square = matrix[row][y]
                steps.append(current_square[0])
                history.append(current_square)
                return current_square
    
    history.pop()
    current_square = history[len(history)-1]

# Loop through the possibilities.

def solve():

    global current_square, goal
    while (current_square != goal) or (24 not in steps):
        try: next_step(current_square[3], current_square[4])
        #In Case2 (puzzle2) has no solution. So print NO SOLUTIONS instead a blank line
        except: return "No solution."
        # print(current_square)
        # print(f"steps: {steps}")

    answer = []

    for i in range (len(history)):
        answer.append(history[i][0])
    
    return f"\nThe answer is: {answer}"

print(solve())
