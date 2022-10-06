def stones(n, a, b):
    # Write your code here
    s = set()
    for i in range(n):
        s.add(i*a + (n-1-i)*b)
        
    return sorted(list(s))