try:
    my_input = input('Enter a number: ')
    my_number = int(my_input)
    print(f'User given number is {my_number}')
except TypeError:
    print('Normal flow of execution is disturbed')
    print('Type of the data mis-matched')
except IndexError:
    print('Normal flow of execution is disturbed')
    print('You tried to access data from outside the List')
except:
    print('Normal flow of execution is disturbed')
    print('Some error occured during runtime')
print('The normal flow of execution is continued...')