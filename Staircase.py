def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        a = ' '*(n-i)
        b = '#'*i
        print(a+b)

# example
staircase(6)