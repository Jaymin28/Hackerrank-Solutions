def bonAppetit(bill, k, b):
    # Write your code here
    total = 0
    for i in range(0,len(bill)):
        if i == k :
            continue
        total += bill[i]
        
    x = int(total/2)
    y = b-x
    if x == b:
        print('Bon Appetit')
    else :
        print(y)