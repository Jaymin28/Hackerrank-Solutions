def pageCount(n, p):
    # Write your code here
    num_of_pages = p//2
    total_num_pages = n//2
    from_front = num_of_pages
    from_back = total_num_pages - from_front
    return (min(from_front,from_back))