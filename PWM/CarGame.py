helpMessage=''
started=False
while True:
        helpMessage = input('>').upper()

        if helpMessage == 'START':
            if started:
                print('Already started')
            else:
                started=True
                print('Getting Started')

        elif helpMessage == 'STOP':
            if not started:
                print('Already Stoped')
            else:
                started=False

                print('Stop')

        elif helpMessage == 'HELP':
            print('''start - to start the car 
            \nstop - To stop the car 
            \nquit - to exit''')
        elif helpMessage=='QUIT':
            break
        else:
            print('I dont Understand')
