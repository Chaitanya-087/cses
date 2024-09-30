grid=[input() for _ in range(8)]

def is_valid(grid,x, y):
    return 0 <= x < 8 and 0 <= y < 8 and grid[x][y] == '.'

def solve(grid,x,cols,diags1,diags2):
    if x == 8:
        return 1
    count = 0
    for y in range(8):
        if is_valid(grid,x,y) and not cols[y] and not diags1[x+y] and not diags2[x-y+7]:
            cols[y] = diags1[x+y] = diags2[x-y+7] = True
            count += solve(grid,x+1,cols,diags1,diags2)
            cols[y] = diags1[x+y] = diags2[x-y+7] = False
    return count

cols = [False]*8
diags1 = [False]*15
diags2 = [False]*15

print(solve(grid,0,cols,diags1,diags2))