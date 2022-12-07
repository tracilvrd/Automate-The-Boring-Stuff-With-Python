print('What is your name?' )
myName = input()
print('How old are you?')
myAge = input()
myAge = int(myAge)
if myName == 'Alice':
    print('Hi, Alice')
elif myAge < 12:
    print('You are not Alice, kiddo')
elif myAge > 100 and myAge < 200:
    print('You are not Alice, grannie')
elif myAge > 200 and myAge < 3000:
    print('When did you become a vampire Alice?')
else:
    print('Hello, stranger')
