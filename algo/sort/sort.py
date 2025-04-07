
# 冒泡排序[不稳定]
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 快速排序[不稳定]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)





if __name__ == "__main__" :
    arr = [4, 5, 1, 2, 3]
    print(bubble_sort(arr))

    arr = [3, 4, 1, 2, 5]
    print(quick_sort(arr))

