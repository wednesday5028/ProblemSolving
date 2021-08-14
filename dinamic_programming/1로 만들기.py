import math

d = [0, 0, 1, 1, 2, 1]

x = int(input())

#해당 숫자보다 아래인 숫자로 가는 연산 + 1, 그리고 해당숫자에서 1로 가는 연산 (ai-1) 이 둘을 더한값이 정답
#f(n) = 1 + min(f(n/5), f(n/3), f(n/2), f(n-1))
for i in range(6, x + 1):
    #조건들: 5로 나누는 경우, 3으로 나누는 경우, 2로 나누는 경우, 1을 빼는경우 (각 경우가 존재할지 안할지 모르기 때문에 무한대를 넣어서 없는 존재로 만듬)
    one, two, three, four = math.inf, math.inf, math.inf, d[i-1]
    if i % 5 == 0:
        one = d[i//5]
    if i % 3 == 0:
        two = d[i//3]
    if i % 2 == 0:
        three = d[i//2]
    d.append(1+min(one, two, three, four))
print(d[x])