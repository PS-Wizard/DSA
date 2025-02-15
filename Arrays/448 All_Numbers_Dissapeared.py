def findDisappearedNumbers(nums):
    return list({i for i in range(1,len(nums)+1)}-set(nums))

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))



      
