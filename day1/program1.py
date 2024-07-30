# Check if the user given number is Perfect Square or not.
import math

input_number = int(input("Enter a number to check if it is Perfect Square: "))
root_number = int(math.sqrt(input_number))
root_number_square = root_number * root_number
if root_number_square == input_number:
    print(f'{input_number} is Prefect Square')
else:
    print(f'{input_number} is not a Prefect Square')
