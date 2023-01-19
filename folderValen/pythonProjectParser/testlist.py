mass1 = list()
mass1.append('b|A')
mass1.append('c||a1')
mass1.append('b||a2')
mass1.append('c|A1')
table = set(list(mass1))
mass1 = []

for el in table:
    mass1.append(el.split('|'))
i = 1
while i < len(mass1):
    if mass1[i][0] == mass1[i - 1][0]:
        print(mass1[i][0])
    i += 1
