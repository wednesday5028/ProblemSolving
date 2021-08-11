def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return  binary_search(array, target, mid + 1, end)


N = int(input())
data_list = list(map(int, input().split()))
data_list.sort()

M = int(input())
target_list = list(map(int, input().split()))
target_list.sort()

for target in target_list:
    print(binary_search(data_list, target, 0, N-1), end=" ")