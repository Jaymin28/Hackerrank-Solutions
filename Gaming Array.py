def gamingArray(arr):
    # Write your code here
    mx = 0
    count = 0
    for i in arr:
        if i > mx:
            mx = i
            count += 1
        
    if count % 2 != 0:
        return 'BOB'
    else :
        return 'ANDY'