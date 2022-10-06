def jimOrders(orders):
    # Write your code here
    from bisect import insort
    sequence = []
    
    for ind, el in enumerate(orders, 1):
        time = sum(el)
        insort(sequence, (time, ind))


# enumerate gives a list of tuples with element and index wich you given with argument like (orders, 1) here index start from 1
# insort function intesrting and sorting list at same time when you give appropriate element