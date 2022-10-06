def gridChallenge(grid):
    # Write your code here
    grid = [list(row) for row in grid]
    n = len(grid)
    c = len(grid[0])
    for i in range(n):
        grid[i].sort()
    
    for j in range(c):
        for i in range(1, n):
            if not grid[i-1][j] <= grid[i][j]:
                return 'NO'
    return 'YES'