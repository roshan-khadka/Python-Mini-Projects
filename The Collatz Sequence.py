#: The Collatz Sequence - "the simplest impossible math problem"
#: Automate the boring stuff with the Python

def collatz_sequence(number):
    if number % 2 == 0:
        print(number // 2)
        return (number // 2)
    elif number % 2 != 0:
        print(number * 3 + 1)
        return (number * 3 +1)
try:
    n = int(input("Please type a number: "))
    while n != 1:
        n = collatz_sequence(n)
except ValueError:
    print("It is not an integer!")
