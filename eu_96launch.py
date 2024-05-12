import eu_96 as sudoku
x=0
with open('0096_sudoku.txt') as f1:
    for i in range(50):
        grid  = []
        for _ in range(10):
            grid.append(f1.readline().strip())
        print(i)
        x += int(sudoku.play(grid[1:]))

print(x)