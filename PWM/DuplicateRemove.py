numbers=[1,2,5,4,2,1]
unique=[]
for item in numbers:
    if item not in unique:
        unique.append(item)
print(unique)