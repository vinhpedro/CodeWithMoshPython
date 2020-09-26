weight=int(input('Enter your weight'))

dis=input('(L)bs or (k)g ?')

if dis.upper()=='L':
    print(f'You are {weight*0.45} kg')
elif dis.upper()=='K':
    print(f'You are {weight/0.45} pound')
else:
    print('Not Fine')