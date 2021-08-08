N = int(input())
dic = {}
for i in range(N):
    name, score = input().split(" ")
    dic[name] = score

sorted_dic = sorted(dic.items(), key = lambda x:x[1])

for i in range(N):
    print(sorted_dic[i][0], end=" ")
