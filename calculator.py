import math
while True:
    number_one = input('Enter your first number\n')
    opperator = input('Enter your opperetor\n')
    number_two = input('Enter second number\n')

# do the opperations
    if opperator == '+':
        total = int(number_one) + int(number_two)
    elif opperator == '-':
        total = int(number_one) - int(number_two)
    elif opperator == 'x':
        total = int(number_one) * int(number_two)
    elif opperator == '/':
        total = int(number_one) / int(number_two)
    elif opperator == '^':
        total = int(number_one) ** int(number_two)
    elif opperator == 'Square Root':
        number_two = 0
        total = math.sqrt(int(number_one)) + number_two
    else:
        total = 'Error'
    print(total)
    stop = input('Do you wish to quit (y , n)?\n')
    if stop == 'y':
        break
    elif stop == 'n':
        pass