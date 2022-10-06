def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count = 0
    while s >= p:
        s -= p
        count += 1
        p = max(m,p-d)
    return count