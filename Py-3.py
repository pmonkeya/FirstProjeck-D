import random
symbols = '深夜花园里四处静悄悄只有风儿在轻轻唱夜色多么好心儿多爽朗在这迷人的晚上小河静静流微微泛波浪水面映着银色月多么幽静的晚上我的心上人坐在我身旁默默看着我不作声我想对你讲但又难为情多少话儿留在心上长夜快过去天色蒙蒙亮衷心祝福你好姑娘但愿从今后你我永不忘莫斯科郊外的晚上'


with open('china.txt', 'wb')
    weigh = 0
    maxx = 100*1024*1024
    while True:
        info = random.choice(symbols)
        info = info.encode('UTF-8')
        weigh += len(info)
        file.write(info)
        if weigh >= maxx:
            break
    