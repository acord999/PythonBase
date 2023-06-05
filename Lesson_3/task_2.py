lst = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input())
res = [lst[0]]
for num_1 in lst:
    near_1 = abs(x - num_1)
    for num_2 in res:
        near_2 = abs(x - num_2)
        if near_1 < near_2:
            res.remove(num_2)
            res.append(num_1)
        elif near_1 == near_2 and num_1 not in res:
            res.append(num_1)


print(sorted(res))
