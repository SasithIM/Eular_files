with open('0096_sudoku.txt') as f1:
    for i in range(4):
        grid  = []
        for _ in range(10):
            grid.append(f1.readline().strip())
        print(i)
        print(grid[1:])


# 1 3 7 2 5 6 8 4 9
# 9 2 8 3 1 4 5 6 7
# 4 6 5 8 9 7 3 1 2
# 6 7 3 5 4 2 9 8 1
# 8 1 9 6 7 3 2 5 4
# 5 4 2 1 8 9 7 3 6
# 2 5 6 7 3 1 4 9 8
# 3 9 1 4 2 8 6 7 5
# 7 8 4 9 6 5 1 2 3