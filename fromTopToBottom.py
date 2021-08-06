N = int(input())

_list = []
for i in range(N):
    _list.append(int(input()))

rev_list = map(str,sorted(_list, reverse=True))
print(" ".join(rev_list))