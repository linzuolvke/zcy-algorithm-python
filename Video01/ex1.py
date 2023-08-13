# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 选择排序
def select_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                # arr[i], arr[j] = arr[j], arr[i]
                # 亦或
                arr[i] = arr[i] ^ arr[j]
                arr[j] = arr[i] ^ arr[j]
                arr[i] = arr[i] ^ arr[j]


if __name__ == "__main__":
    # 冒泡排序
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", arr)
    bubble_sort(arr)
    print("冒泡排序后的数组:", arr)
    # 选择排序
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", arr)
    select_sort(arr)
    print("选择排序后的数组:", arr)
