def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


def userInput():
    while True:
        try:
            return int(input())
        break


except ValueError:
    print('Error: Number not a valid integer number.')
    print('Please select a valid integer number...')


print('Select any number.')
myNumber = userInput()
while myNumber != 1:
    myNumber = collatz(myNumber)
    print(myNumber)
