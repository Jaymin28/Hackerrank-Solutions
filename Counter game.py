import math

def counterGame(n):
    # Write your code here
    def get_mask(n):
        return 1 << math.floor(math.log2(n)) 
        
        # left shift to the 1 returns a decimal number = 2**math.floor(math.log2(n))
    
    winner = 0
    while n > 1:
        mask = get_mask(n)
        if mask == n:
            n = n/2
        else :
            n -= mask
        
        winner ^= 1
    
    if winner == 1:
        return 'Louise'
    else :
        return 'Richard'