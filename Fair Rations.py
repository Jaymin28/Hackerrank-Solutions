def fairRations(B):
    # Write your code here
    if sum(B) % 2 == 1:
        return 'NO'
    total = 0
    for i in range(len(B)-1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i+1] += 1
            total += 2
    return str(total)