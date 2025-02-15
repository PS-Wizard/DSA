def smallerNumbersThanCurrent(arr):
    sort = sorted(arr)
    return [sort.index(i) for i in arr];

print(smallerNumbersThanCurrent([1,2,3,4,5]))

