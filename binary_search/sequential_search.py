
def sequential_search(n, target, array):
    #각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재 원소가 찾고자하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1
        # 현재의 위치를 반환, 인덱스는 0부터 시작하니까