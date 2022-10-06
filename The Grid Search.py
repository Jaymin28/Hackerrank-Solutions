def gridSearch(G, P):
    # Write your code here
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    
    def check(i, j):
        for x in range(r):
            if P[x] != G[x+i][j:j+c]:
                return False
        return True
    
    for i in range(R):
        for j in range(C):
            if G[i][j] == P[0][0]:
                if check(i, j):
                    return 'YES'
    return 'NO'