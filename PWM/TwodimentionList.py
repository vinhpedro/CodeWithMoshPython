matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])

for list in matrix:
    for item in list:
        print(item)

matrix[0][2]=10
print(matrix[0][2])