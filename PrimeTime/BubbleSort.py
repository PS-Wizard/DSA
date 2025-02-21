arr = [1,23,2,45,1,1,2,32,1,2,3,5,1,2,3,4,]

def BubbleSort():
    length = len(arr)
    for i in range(length):
        for j in range (length-1-i):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

BubbleSort()
