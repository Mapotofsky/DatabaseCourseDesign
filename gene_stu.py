import random

Snums_year = ['2018', '2019']
Snums_majc = {
    '0601': ['01', '02'],
    '0602': ['01', '02', '03'],
    '0603': ['01', '02', '03'],
    '0604': ['01'],
    '0605': ['01']
}
Sadd = {
      '北京': ['朝阳区', '海淀区', '通州区'],
      '浙江': ['嘉兴市', '温州市', '宁波市', '杭州市'],
      '江苏': ['南京市', '苏州市'],
      '上海': ['松江区', '宝山区', '金山区']
}

count = 1
for y in Snums_year:
    for m in Snums_majc.keys():
        for c in Snums_majc[m]:
            s = 7
            if y == '2018':
                s = 2
            count_cl = 1
            for i in range(s):
                clnum = str(count_cl)
                clnum = clnum.zfill(2)
                Snum = f"{y}{m}{c}{clnum}"
                count_cl += 1

                countnum = str(count)
                countnum = countnum.zfill(2)
                Sname = f"S{countnum}"
                count += 1

                Ssex = '男'
                if random.random() > 0.5:
                    Ssex = '女'

                Sage = 20

                Spro = random.choice(list(Sadd.keys()))
                Scity = random.choice(Sadd[Spro])

                print(f"('{Snum}', '{m}', '{c}', '{Sname}', '{Ssex}', '{Sage}', '{Spro}', '{Scity}', null),")
