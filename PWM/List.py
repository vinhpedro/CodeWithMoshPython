#find Largest Number

numbers=[2,13,28,1,10,7,9,22,13]
largest=numbers[0]

for num in numbers:
    if num>=largest:
        largest=num
print(largest)

names=['Aohona','Dipu','Mony']
print(names[0])
print(names[:2])
print(names[:])
print(names[0:])
names[2]='Tamanna'
print(names[2])
print(names)
