try:
    age=int(input('>'))
    print(age)
    total=2000/age

except ZeroDivisionError:
    print('Cant vdide by Zero')
except ValueError:
    print('Invalid input ')