def shax_i_ban():
    a12 = []
    ch = 0
    for i in range(8):
        b = []
        for j in eange(8):
            if ch%2 == 0:
                b.append (j%2)
            else:
                b.append((j+1)%2)
    a12.append(b)
    ch += 1
    return a12
print(shax_i_ban)

