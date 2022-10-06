def circularArrayRotation(a, k, queries):
    # Write your code here
    n = len(a)
    l = list()
    for q in queries:
        l.append(a[(n-k+q)%n])
    return l

# Explanation

# Solution in Python.
# First, we will declare the length of array a in a variable n in the given function.


# Instead of circularly rotating the array manually, if we reduce the magnitude of given number of rotations i.e k from the length of array i.e n we will get a number which will be the first index of the array a after the k right circular rotations rotations, that is, the expression

# n-k

# Now, we will add the queries or the indices to check in the array after performing the k right circular rotations. Therefore the expression will be

# n-k+q

# Albeit, if the value of expression (n-k+q) exceeds n-1 the array will get out of bounds. In order to commence the index from the start will have to add a modulus of n after the expression. Thus the expression, for the qth index of array a after k right circular rotation is

# (n-k+q)%n