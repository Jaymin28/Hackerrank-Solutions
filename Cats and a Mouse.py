def catAndMouse(x, y, z):
    X = abs(x-z)
    Y = abs(y-z)
    if X == Y:
        return 'Mouse C'
    elif X < Y:
        return 'Cat A'
    elif Y < X:
        return 'Cat B'