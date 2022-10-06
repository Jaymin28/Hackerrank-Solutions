def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    count = 0
    total = 0
    for i in prices:
        total += i
        if total > k:
            break
        else:
            count += 1
    
    return count