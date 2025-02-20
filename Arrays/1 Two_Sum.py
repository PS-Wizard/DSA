def twoSum(arr,target):
    for i,v in enumerate(arr):
        if (target-v) in arr[:i:]:
            return [i,arr.index(target-v)]

print(twoSum([3,3],6))
