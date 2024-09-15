furniture=['table','chair','pen','rack','shelf']
for i in furniture:
    print(i)
print(furniture[2])
furniture.append('book')
print(furniture)
#insert
furniture.insert(3,'cot')
#del
del furniture[2]
#remove
furniture.remove('table')
furniture.pop()
print(furniture)
print(len(furniture))