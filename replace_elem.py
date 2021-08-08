N, K = map(int,input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

new_arr_a = sorted(arr_a)
new_arr_b = sorted(arr_b, reverse=True)

for i in range(K):
    new_arr_a[i] = new_arr_b[i]

print(sum(new_arr_a))