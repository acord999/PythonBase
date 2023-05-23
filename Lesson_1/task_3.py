num = int(input())
n = input().strip()
print(['NO', 'YES'][sum(list(map(int, n[:3]))) == sum(list(map(int, n[3:])))])
