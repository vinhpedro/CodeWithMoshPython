name=input('Enter your name')


if len(name)<3:
    print('Name mut be at least 3 char')
elif len(name)>50:
    print('Name must be maximum 50 char')
else:
    print('Okay')