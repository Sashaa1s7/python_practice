spisok = ['mother', 'Daddy', 'sIster']
spisok = ['bBb', 'aaaaaa', 'word']

sp =[]
row = "tru"

while row:
    row = input()
    if row:
        sp.append(row) #sp.append(row.upper())


print(sp)

print(*sorted(sp, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')
