# def binary_search(array, target, start, end, M):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if check(array, mid, M):
#         return mid
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽을 확인, 끝점을 중간지점 - 1
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
#
#
# def check(array, H, target):
#     result = []
#     for i in array:
#         if i - H <= 0:
#             continue
#         else:
#             result.append(i - H)
#         if sum(result) != target:
#             result.clear()
#         else:
#             return True
#     return False

N, M = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

