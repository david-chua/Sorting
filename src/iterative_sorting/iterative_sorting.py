# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if (arr[smallest_index] > arr[j] ):
                smallest_index = j
        # TO-DO: swap
        if (smallest_index > cur_index):
            temp = arr[smallest_index]
            arr[smallest_index] = arr[cur_index]
            arr[cur_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]= temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if maximum == -1:
        maximum = max(arr)
    ## initializes an array of length maximum + 1 and everything starts with 0
    counts = [0] * (maximum + 1)
    for item in arr:
        counts[item] += 1

    for number 



    return arr
