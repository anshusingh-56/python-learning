# Program to find minimum number using args.

def minimum(*nums):
    min = nums[0]

    for i in nums:
        if i<min:
            min = i

    print("Minimum no is ",min)

minimum(11,22,33)
minimum(4,5,23,45,22,55,72,11,34)
