orderedArr = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(arr,toSearch):
    mid = int(len(arr) / 2)
    print(f'Checking: {arr}')
    if not arr:
        return False

    if arr[mid] == toSearch:
        return True
    
    if arr[mid] < toSearch:
        return binarySearch(arr[mid:],toSearch)

    if arr[mid] > toSearch:
        return binarySearch(arr[:mid],toSearch)
     

print(binarySearch(orderedArr,-1))
