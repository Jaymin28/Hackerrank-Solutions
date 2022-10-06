def migratoryBirds(arr):
    # Write your code here
    count = [0]*len(arr)
    for i in arr:
        count[i] += 1
    return count.index(max(count))

# Explanation

#First you initialize an array like this arr = [0,0,0,0,0,0] which can also be written as [0]*6
#Now when you see bird 1 you will increment index 1 by 1, if you see bird 2 you will increment index 2 and so and so.
#For example, you saw the following birds 2,2,2,3,3,5  then our array will become something like this

#[0,0,3,2,0,1]

#As you you may have noticed.
#Index 1 increased by 0 since bird 1 is seen 0 time
#Index 2 increased by 3 since bird 2 is seen 3 times
#Index 3 increased by 2 since bird 3 is seen 2 times
#Index 4 increased by 0 since bird 4 is seen 2 times
#Index 5 increased by 1 since bird 5 is seen 1 time#

#Now max(arr) will give us 3, that is the count of the most seen bird.#


#arr.index(max(arr)) or arr.index(3) will give us 2 which means the bird in index 2 is seen the maximum number of times.