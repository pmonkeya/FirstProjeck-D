def count_elem(file_name):
    answ = []
    for i in range (10):
        answ.append([i, 0])
    with open(file_name, 'r') as files:
        for i in files:
            i = i.strip()
            for j in i:
                if j.isdigit():
                    j = int(j)
                    answ[j][1] += 1
    return answ


print(count_elem('pi.txt'))