def gemstones(arr):
    # Write your code here
    superset = set(arr[0])
    for i in arr:
        superset = superset & set(i)
    return len(superset)