import random

n = 4

# Generate random 4x4 grid
# 0 = clean, 1 = dirty
grid = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]

print("Random 4x4 Grid:")
for row in grid:
    print(row)

# Vacuum starts at top-left
r = 0
c = 0

actions = []

# Visit every cell in zig-zag order
for i in range(n):

    if i % 2 == 0:
        # Move right
        for j in range(n):
            while c < j:
                c += 1
                actions.append("RIGHT")

            if grid[i][j] == 1:
                actions.append("CLEAN")
                grid[i][j] = 0

    else:
        # Move left
        for j in range(n - 1, -1, -1):
            while c > j:
                c -= 1
                actions.append("LEFT")

            if grid[i][j] == 1:
                actions.append("CLEAN")
                grid[i][j] = 0

    # Move down to next row
    if i < n - 1:
        r += 1
        actions.append("DOWN")

print("\nSequence of actions:")
print(" -> ".join(actions))

print("\nFinal Grid:")
for row in grid:
    print(row)


