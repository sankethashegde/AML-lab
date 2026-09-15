# 5]  Implementation of the quicksort algorithm in Python. [3,6,8,10,1,2,1]

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

numbers = [3, 6, 8, 10, 1, 2, 1]
print("Original List:", numbers)
print("Sorted List:", quicksort(numbers))