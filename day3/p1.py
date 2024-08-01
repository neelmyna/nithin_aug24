import math

squares3 = list(map(lambda x: ((x**2) + int(math.sqrt(x))), range(10)))
print('Squares3 = ', squares3)

input_numbers = list(map(int, input().split()))
print(input_numbers)

'''
input_numbers = list(map(int, input().split()))

step1: input()
Read a string

step2: input().split()
The string read by input() is split on spaces, because default delimiter(argument) of split is space

input.split('@') # The delimiter here is '@'
12@1@124@34@57
'12', '1', '124', '34', '57'

delimiter: The character that seperates 2 values

step4:
map(int, input().split())
The many strings after applying split() on the input string is passed one by one to map()
The map() is converting all the values (strings) into int and later all these int values we are using to create a list.
'''
