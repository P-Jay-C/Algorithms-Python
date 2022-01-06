def search(arr, search_Element):
    left = 0
    length = len(arr)
    position = -1
    right = length - 1

    for left in range(0,right,1):

        if (arr[left] == search_Element):
            position = left
            print("Element found in array at ", position+1)
            break

        if (arr[right] == search_Element):
            position = right
            print("Element found in array at ", position+1)
            break

        if(position == -1):
            print("Element not found in array.")


arr = [1,2,3,4,5]
search_Element = 5

search(arr, search_Element = search_Element)