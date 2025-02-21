orderedArr = [1,2,3,4,5,6,7,8,9,10]
toSearch = -1

# def binarySearch(low,high):
#     midPoint = (low + high)//2
#
#     print(f'Searching: {orderedArr[low:high]}')
#     if low > high:
#         return None
#
#     if orderedArr[midPoint] == toSearch:
#         return midPoint
#
#     if orderedArr[midPoint] > toSearch:
#         high = midPoint -1
#
#     if orderedArr[midPoint] < toSearch:
#         low = midPoint + 1
#
#     return binarySearch(low,high)
#
# print(binarySearch(0,len(orderedArr)-1))

def binarySearch(low,high):
    while (low <= high):
        midPoint = (low + high) // 2 

        if orderedArr[midPoint] == toSearch:
            return midPoint

        if orderedArr[midPoint] > toSearch:
            high = midPoint - 1

        if orderedArr[midPoint] < toSearch:
            low = midPoint + 1

    return None

print(binarySearch(0,len(orderedArr)-1))
