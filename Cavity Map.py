def cavityMap(grid):
    # Write your code here
    leng = len(grid)
    output = [[0]*leng for _ in range(leng)]
    
    for ind in range(leng):
        for jnd in range(leng):
            if (0 < ind < leng-1 and 0 < jnd < leng-1 and
               grid[ind][jnd] > grid[ind+1][jnd] and
               grid[ind][jnd] > grid[ind-1][jnd] and
               grid[ind][jnd] > grid[ind][jnd+1] and
               grid[ind][jnd] > grid[ind][jnd-1]):
                output[ind][jnd] = 'X'
            else:
                output[ind][jnd] = grid[ind][jnd]
    
    return list(map(lambda x: ''.join(x), output))