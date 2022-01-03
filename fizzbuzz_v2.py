printing = 0
num = 0
while True:
    printing = 0
    num = num + 1
    if num%15  == 0:
        print('FizzBuzz')
        printing = 1
    elif num % 5 == 0:
        if printing == 0:
            print('Buzz')
            printing = 1
    elif num % 3 == 0:
        if printing == 0:
            print('Fizz')
            printing = 1
    elif printing == 0:
        print(num)
