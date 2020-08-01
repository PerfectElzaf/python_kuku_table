kuku = []
for i in range(1, 10):
    for j in range(1, 10):
        if len(str(i*j)) < 2:
            result = str(i*j).rjust(2, " ")
        else:
            result = str(i*j)
        kuku.append(result)

kukuList = [kuku[i:i+9] for i in range(0, len(kuku), 9)]

for i in kukuList:
    for j in i:
        print('{} '.format(j), end='')
    print('\n')
