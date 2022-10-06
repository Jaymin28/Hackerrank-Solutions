def birthdayCakeCandles(candles):
    # Write your code here
    largest = -1
    count = 0
    for i in candles:
        if i > largest:
            largest = i
    for j in candles:
        if j == largest:
            count += 1
    return count