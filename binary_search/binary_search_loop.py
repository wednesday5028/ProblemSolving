def binary_search(array, target, start, end):
    # 시작점과 끝점이 같거나 시작점이 끝점보다 커질 때, 즉 교차할 때는 값이 없는거..
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            #타겟이 중간보다 왼쪽에 있을 때 끝 값을 중간값의 -1로
            end = mid - 1
        else:
            start = mid + 1
    #값을 못찾고 루프를 빠져나오면
    return None