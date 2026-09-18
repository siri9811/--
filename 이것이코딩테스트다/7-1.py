# 이진탐색 구현하기
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr,target, mid + 1, end)

arr = [1,2,3,7,8,9,15,77,93]

print(binary_search(arr, 99, 0, len(arr) - 1))

# 0, 8, 4 -> 5, 8, 6 -> 7, 8, 7