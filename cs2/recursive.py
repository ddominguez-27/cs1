


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def summation(n):
    if n > 0:
        return n + summation(n-1)
    else:
        return 0


def main():
    #choice = input("Please select a choice")
    print(factorial(5))
    print(summation(10))


main()