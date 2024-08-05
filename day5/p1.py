class XShapeException(Exception):
    def printError(self, errorMessage):
        print(errorMessage)

number_of_lines = int(input('Enter number of lines to print X shape: '))
try:
    if number_of_lines % 2 == 0:
        raise XShapeException
    else:
        # Logic to draw the X shape
        print('Consider X shape is drawn')
except XShapeException as e:
    try:
        e.printError('Invalid input was given')
        e.removeError()
    except:
        print('Some error occured while handling the exception')
