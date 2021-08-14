n = int(input())
data = list(map(int, input().split()))


# ai를 i번째 식량 창고 까지의 최적의 해라고 하면
# i-1번째 창고까지의 해와, i-2 창고까지의 해와 자신의 창고를 더했을 때 해중 제일 큰 값이 정답이다.
d = [0] * 100
d[0] = data[0]
d[1] = max(d[0], data[1])

for i in range(2, n + 1):
    d[i] = max(d[i-1], d[i-2] + data[i])

print(d[n-1])
