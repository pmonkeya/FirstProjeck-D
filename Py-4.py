import random,time
symbols = '深夜花园里四处静悄悄只有风儿在轻轻唱夜色多么好心儿多爽朗在这迷人的晚上小河静静流微微泛波浪水面映着银色月多么幽静的晚上我的心上人坐在我身旁默默看着我不作声我想对你讲但又难为情多少话儿留在心上长夜快过去天色蒙蒙亮衷心祝福你好姑娘但愿从今后你我永不忘莫斯科郊外的晚上'




data[]
maxx = 10*1024*1024
for in range(3):
    weigh = 0
    while True:
        element = random.choice(symbols)
        line += element
        weigh += len(element)
        if weigh >= maxx:
            break
    data.append(line)
print('qwerty')
print(data)

file_max = 3*1024*1024*1024
ch = 0

with open('china.txt','wb')as file:
    while True:
        a = random.choice(data)
        a = a.encode
        