class Sudoku:
    def __init__(self,temp_grid:list) -> None:
        self.done = False
        self.grid = []
        self.filled_xy = []
        for line in temp_grid:
            self.grid.append([int(n) for n in line])
    
    def fill(self) -> None:
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    self.grid[x][y]=list(range(1,10))
                else:
                    self.grid[x][y] = [self.grid[x][y]]
                    self.filled_xy.append((x,y,self.grid[x][y][0]))
        for (x,y,a) in self.filled_xy:
            self.remove_filled(x,y,a)

    def solve(self) -> bool:
        l_before = len(self.filled_xy)
        for x in range(9):
            for y in range(9):
                t = self.grid[x][y]
                a = t[0]
                if len(t)<2 and (x,y,a) not in self.filled_xy:
                    self.filled_xy.append((x,y,a))
                    self.remove_filled(x,y,a)
                    # print(f'solved {x,y,a}')
        if len(self.filled_xy)-l_before == 0:
            return True
        else:
            return False
        
    def solve2(self) -> bool:
        solved = 0
        for x in range(9):
            tx = self.grid[x]
            for y in range(9):
                ty = tx[y]
                if len(ty)>1:
                    t1 = set()
                    t2 = set(ty)
                    for t in tx:
                        if t!=ty:
                            t1.update(t)
                    t3 = t2-t1
                    if len(t3)==1:
                        self.grid[x][y] = list(t3)
                        solved+=1

        if solved==0:
            return True
        else:
            return False
        
    def solve3(self) -> bool:
        solved = 0
        for y in range(9):
            ty = [self.grid[x][y] for x in range(9)]
            for x in range(9):
                tx = ty[x]
                if len(tx)>1:
                    t1 = set()
                    t2 = set(tx)
                    for t in ty:
                        if t!=tx:
                            t1.update(t)
                    t3 = t2-t1
                    if len(t3)==1:
                        self.grid[x][y] = list(t3)
                        solved+=1

        if solved==0:
            return True
        else:
            return False


    def remove_filled(self,x,y,a) -> None:
        '''remove 'a' from line x'''
        for i in range(9):
            if i!=y:
                t = self.grid[x][i]
                if len(t)>1:
                    try:
                        t.remove(a)
                    except:
                        pass
            if i!=x:
                t = self.grid[i][y]
                if len(t)>1:
                    try:
                        t.remove(a)
                    except:
                        pass
        # print(f'from row {y} removed {a}')
        # print(f'from line {x} removed {a}')

        for i in range(9):
            tx,ty = (x//3)*3+(i//3),(y//3)*3+(i%3)
            if tx!=x and ty!=y:
                t = self.grid[tx][ty]
                if len(t)>1:
                    try:
                        t.remove(a)
                    except:
                        pass
        # print(f'from box {(x//3)+(y//3)} removed {a}')


    def print_solved(self) -> tuple[int, str]:
        output = ''
        tofill = 0
        for line in self.grid:
            for pos in line:
                if len(pos)<2:
                    try:
                        output+=f'{pos[0]}'
                    except:
                        output+='N'
                else:
                    output+='0'
                    tofill+=1
            output+='\n'
        # print(f'---to_fill = {tofill}')
        # print(f'---filled = {len(self.filled_xy)}')
        return tofill,output

    def print_grid(self) -> None:
        for line in self.grid:
            print(line)




def format_grid(str1:str) -> list:
    return [line for line in str1.split('\n')]


def play(temp_g) -> int:

    prev_left = 0
    grid1 = Sudoku(temp_g)
    grid1.fill()
    left = 1
    while left>0:
        prev_left = left
        while not grid1.solve():
            pass
        left,output = grid1.print_solved()
        if left == 0:
            break
        while not grid1.solve2():
            pass
        left,output = grid1.print_solved()
        while not grid1.solve():
            pass
        left,output = grid1.print_solved()
        if left == 0:
            break
        while not grid1.solve3():
            pass
        left,output = grid1.print_solved()
        if left == prev_left:
            play2(temp_g)
            # return -1
            break
    print(output)
    return int(f'{grid1.grid[0][0][0]}{grid1.grid[0][1][0]}{grid1.grid[0][2][0]}')

def play2(temp_g) -> int:

    prev_left = 0
    grid1 = Sudoku(temp_g)
    grid1.fill()
    left = 1
    while left>0:
        prev_left = left
        while not grid1.solve():
            pass
        left,output = grid1.print_solved()
        if left == 0:
            break
        while not grid1.solve2():
            pass
        left,output = grid1.print_solved()
        while not grid1.solve():
            pass
        left,output = grid1.print_solved()
        if left == 0:
            break
        while not grid1.solve3():
            pass
        left,output = grid1.print_solved()
        if left == prev_left:
            play3(temp_g)
            # return -2
            break
    print(output)
    return int(f'{grid1.grid[0][0][0]}{grid1.grid[0][1][0]}{grid1.grid[0][2][0]}')

def play3(temp_g) -> int:

    prev_left = 0
    grid1 = Sudoku(temp_g)
    grid1.fill()
    left = 1
    while left>0:
        prev_left=left
        while not grid1.solve():
            pass
        left,output = grid1.print_solved()
        if left == 0:
            break
        grid1.solve2()
        left,output = grid1.print_solved()
        if left == 0:
            break
        grid1.solve()
        left,output = grid1.print_solved()
        if left == 0:
            break
        grid1.solve3()
        left,output = grid1.print_solved()
        if left == 0:
            break
        if left == prev_left:
            print("can't solve")
            return -3
    print(output)
    return int(f'{grid1.grid[0][0][0]}{grid1.grid[0][1][0]}{grid1.grid[0][2][0]}')



# print(grid1.filled_xy)
print(play(['030050040', '008010500', '460000012', '070502080', '000603000', '040109030', '250000098', '001020600', '080060020']))

# g1 = Sudoku(['030050040', '008010500', '460000012', '070502080', '000603000', '040109030', '250000098', '001020600', '080060020'])
# g1.fill()
# g1.solve()
# g1.solve()
# g1.print_grid()
# print()
# g1.solve2()
# g1.print_grid()
# print()
# g1.solve()
# g1.print_grid()
# print()
# g1.solve3()
# g1.print_grid()
# print()
# g1.solve()
# g1.print_grid()
# print()
# g1.solve2()
# g1.print_grid()
# print()
# g1.solve()
# g1.print_grid()
# print()
# g1.solve3()
# g1.print_grid()
# print()
# g1.solve()
# g1.print_grid()