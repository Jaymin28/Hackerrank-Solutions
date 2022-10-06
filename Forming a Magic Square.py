# solution 1
import sys
def formingMagicSquare(s):
    # Write your code here
    import itertools
    s = sum(s, [])
    def is_magic(s):
        for i in range(3):
            if sum(s[i*3:i*3+3]) != 15:
                return False
            if sum(s[i::3]) != 15:
                return False
        if s[0] + s[4] + s[8] != 15:
            return False
        if s[2] + s[4] + s[6] != 15:
            return False
        return True
    
    min_cost = sys.maxsize
    for p in itertools.permutations(range(1,10)):
        cost = sum([abs(p[i] - s[i]) for i in range(len(s))])
        if cost < min_cost and is_magic(p):
            min_cost = cost
         
    return min_cost

# shortcut solution

def formingMagicSquare(s):
    # Write your code here
    import itertools
    s = sum(s, []) # convert 2d into 1d
    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4,               3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1,               5, 9, 6, 7, 2]]
    
    mincost = sys.maxsize
    
    for mag in magic:
        diff = 0
        for i, j in zip(s,mag):
            diff += abs(i-j)
        mincost = min(mincost, diff)
    
    return mincost