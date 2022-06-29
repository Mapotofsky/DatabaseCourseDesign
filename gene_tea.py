import random


def shuffle(lis):
    for i in range(len(lis) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        lis[i], lis[p] = lis[p], lis[i]
    return lis


Ttitles = ['无职称', '助教', '副教授', '教授']

count = 1
for i in range(7):
    num = str(count)
    Tnum = num.zfill(12)

    countnum = num.zfill(2)
    Tname = f"T{countnum}"
    count += 1

    Tsex = '男'
    if random.random() > 0.5:
        Tsex = '女'

    Tage = random.randint(28, 65)

    Ttitle = random.choice(Ttitles)

    Tphone = ['1', '1', '4', '5', '1', '4', '1', '9', '1', '9', '8', '1', '0']
    Tphone = shuffle(Tphone)
    Tph = ''.join(Tphone[:11])

    print(f"('{Tnum}', '{Tname}', '{Tsex}', '{Tage}', '{Ttitle}', '{Tph}'),")
