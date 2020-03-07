with open ('pi.txt','r') as file:
    fil = file.readlines()
fil2 = []
fil1 = fil [::-1]
with open ('pi2.txt','w') as file:
    for i in fil:
        i = i.strip()
        i = i[::-1]
        file.write(i+'\n')
