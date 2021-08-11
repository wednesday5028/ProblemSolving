def make_rice(array, start, end, M):
    result = []
    for i in range(start, end, 1):
        for rice in array:
            if rice - i <= 0:
                continue
            else:
                result.append(rice - i)
        if sum(result) != M:
            result.clear()
        else:
            return i

test_arr = [10, 15, 17, 19]
print(make_rice(test_arr, test_arr[0], test_arr[-1], 6))
# 시간초과