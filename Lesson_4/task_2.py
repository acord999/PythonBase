n = int(input())
lis = [int(x) for x in input().split()]
lis += lis[:2]
print(max(sum(triplet) for triplet in zip(lis, lis[1:], lis[2:n+2])))

