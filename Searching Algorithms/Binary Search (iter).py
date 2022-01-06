def BinarySearch(arr, l,r,x):
    while r >= l:
        mid = l + (r -l) //2 

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            r = mid -1
        else:
            l = mid + 1

    return -1

arr = [1,2,3,4,5]
x = 2
lenght = len(arr)

result = BinarySearch(arr,0,lenght-1,x)

if result != -1:
    print("Element can be found at index: {}".format(result))
else:
    print("Element can't be found")
