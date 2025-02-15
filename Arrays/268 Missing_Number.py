# First Attempt:
# def missingNumber(nums):
#     for i in range (0,len(nums)+1):
#         if i not in nums:
#             return i
#
# print(missingNumber([3,0,1]))

def missingNumber(nums):
    return sum(range(len(nums)+1))-sum(nums)

print(missingNumber([0,1]))
