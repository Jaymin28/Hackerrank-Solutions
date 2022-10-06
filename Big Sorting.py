def bigSorting(unsorted):
    # Write your code here
    unsorted.sort(key = lambda x: (len(x), x))
    return unsorted