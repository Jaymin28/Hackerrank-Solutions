def beautifulTriplets(d, arr):
    # Write your code here
    count =0
    for i in arr:
        if (i+d in arr) and (i+2*d in arr):
            count += 1
    return count