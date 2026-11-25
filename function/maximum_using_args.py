# Program to find maximum number using args

def maximum(*nums):
    max = nums[0]

    for i in nums:
        if i>max:
            max = i

    print("Maximum no is ",max)

maximum(11,22,33)
maximum(4,5,23,45,22,55,72,11,34)
