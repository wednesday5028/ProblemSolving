array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    #교차하면 반복 끝내고 피봇과 작은 숫자를 바꾼다.
    while left <= right:
        # 피봇보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피봇보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    #마지막까지 교환했더라면 피봇과 작은수(right) 와 교환했을 것이므로 right -1가 끝이다
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) -1)
print(array)

array2 = [7,5,9,0,3,1,6,2,4,8]

def quick_sort_py(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    #for문 돌면서 pivot보다 작은 값들을 왼쪽 리스트에 넣음
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x >= pivot]

    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


print(quick_sort_py(array2))