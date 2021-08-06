array = [7,5,9,0,3,1,6,2,4,8]

#삽입정렬은 두 번째 데이터 부터 시작, 첫 번째 데이터는 그 자체로 정렬되어있다고 판단
for i in range(1, len(array)):
    for j in range(i,0,-1): #인덱스 i부터 1까지 감소하면서 반복하는 문법, 즉 뒤에서부터 비교
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break