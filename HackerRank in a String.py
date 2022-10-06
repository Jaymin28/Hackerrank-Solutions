import re

def hackerrankInString(s):
    # Write your code here
    return 'YES' if re.search('.*'.join(list('hackerrank')),s) else 'NO'

# Explanation

# Answer explanation

# The code

# ".*".join(list("hackerrank"))
# Creates the following regex pattern

#  'h.*a.*c.*k.*e.*r.*r.*a.*n.*k'
#  .* just means "0 or more of any character"

# It's broken down into two parts:

# . - a "dot" indicates any character
# * - means "0 or more instances of the preceding regex token"

# So it matches any word that has hackerrank in it such as

# s ="h--ac++ke---zzz---r--ra??nk"

# Solution 2

def hackerrankInString(s):
    a = 0
    for i in s:
        if a<10 and i == "hackerrank"[a]:
            a+=1
    return "YES" if a==10 else "NO"

for _ in range(int(input())):
    print(hackerrankInString(input()))

# Answer Explanation

# Assume our string is

# "papahopackerank"
# So we will be looping the above string

# for i in "papahopackerank"
# Initially a = 0 means "hackerrank"[0] = "h"

# In our for loop once we find a "h" we will increase a. "papa" is completely ignored

# After finding "h" it will increase a and now "hackerrank"[1] = "a" which means it will start searching "a" in rest of the string then "c" then "k" up to the end.

# if a becomes 9 we can just break the loop and print "YES". Since a = 9 means we have found all letters of hackerrank.

# In our example string, a will become 5 since it will match only up to "hacker". So our program will print "No"