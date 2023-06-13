set1 = set(input().split())
set2 = set(input().split())

common_set = sorted(set1 & set2)

if len(common_set) == 0:
    print("Отсуствуют общие элементы")
else:
    for val in common_set:
        print(val, end=" ")
