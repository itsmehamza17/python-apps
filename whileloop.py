num_of_tries = 0
while num_of_tries != 3:
    username = input('Please insert your username: ')
    password = input('Please insert your password: ')
    if username == 'hamza' and password == '12345':
        print('welcome to your account')
        num_of_tries = 0
        exit()
    else:
        print('error: invalid username or password')    
        num_of_tries +=1
        print('you still have ' + str(3 - num_of_tries) + ' tries left ')