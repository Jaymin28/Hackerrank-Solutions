
# Example of enumerate

# Python program to illustrate enumerate function

# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"
  
# creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)
  
# print ("Return type:", type(obj1))
# print (list(enumerate(l1)))
  
# changing start index to 2 from 0
# print (list(enumerate(s1, 2)))
# Output:
# Return type: 
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

def marsExploration(s):
    # Write your code here
    count = 0
    for i, char in enumerate(s):
        if i % 3 == 1:
            if char != 'O':
                count += 1
        else :
            if char != 'S':
                count += 1
    return count