amount = int(input("Введите кол-во монет>?"))
cnt_0 = 0
cnt_1 = 1
for n in range(amount):
    num = int(input("Положение монеты 0: 0 или 1>?"))
    if num == 0:
        cnt_0 += 1
    elif num == 1:
        cnt_1 += 1
if cnt_0 > cnt_1:
    print(cnt_1)
else:
    print(cnt_0)