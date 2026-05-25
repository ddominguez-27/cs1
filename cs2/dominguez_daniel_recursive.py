"""
Recursive Functions
Author: Daniel Dominguez
Date: 5/20/26
Sources: Spec sheet
Description:  List of functions that all use recursive functions that can be selected from a menu
Log: Graded by Mia, Nad
"""


def factorial(n):
    # Args:
    #     n (int)
    # Return:
    #     n! (int)
    # Description: 
    #    recursive functions create the factorial of a number by multiplying the input number by one less than n, stopping at 1


    if n == 0:
        return 1
    return n * factorial(n - 1)

def summation(n):
    # Args:
    #     n (int)
    # Return:
    #     sum of n (int)
    # Description:
    #     calculates the sum of all whole numbers from n down to 0 using recursion
    
    if n > 0:
        return n + summation(n-1)
    else:
        return 0
    
def exponention(x, n):
    # Args:
    #     x (int)
    #     n (int)
    # Return:
    #     x^n (int)
    # Description:
    #     multiplies the base number x by itself n times recursively, stopping when the power reaches 0
  
    if n == 0:
        return 1
    return x*exponention(x, n-1)

def fibonacci(n):
    # Args:
    #     n (int)
    # Return:
    #     nth Fibonacci number (int)
    # Description:
    #     returns nth number in the fibonacci sequence by adding the two previous numbers together until 1 and 0 are reached
   
    if n == 0:
        return n
    elif n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def digitsum(n):
    # Args:
    #     n (int)
    # Return:
    #     sum of digits (int)
    # Description:
    #     takes the last digit and adds it by the next number down the line through recursion
  
    if n < 10:
        return n
    return digitsum(n//10) + n%10

def digitprod(n):
    # Args:
    #     n (int)
    # Return:
    #     product of digits (int)
    # Description:
    #     takes the last digit and multiplies it by the next number down the line through recursion
    
    if n < 10:
        return n
    return digitprod(n//10)*(n%10)


def product(a, b):
    # Args:
    #     a (int)
    #     b (int)
    # Return:
    #     a*b (int)
    # Description:
    #     performs multiplication through repeated recursive addition of the number a, b times
  
    if b == 0:
        return 0
    return product(a,(b-1)) + a

def rangedsum(n, x):
     # Args:
    #     n (int)
    #     x (int)
    # Return:
    #     sum of range (int)
    # Description:
    #     adds numbers continuously from the upper limit n down to the lower limit base case x
    
    if n == x:
        return x
    return rangedsum((n-1), x) + n

def reversednumber(n):
    # Args:
    #     n (int)
    # Return:
    #     reversed integer (int)
    # Description:
    #     reverses  digits of by moving the last digit of the current number to the highest place value recursively
   
    if n < 10:
        return n
    return((n%10)*(exponention(10,(len(str(n//10))))) + reversednumber(n//10)) 




    


def main():
    # Args:
    #     n/a
    # Return:
    #     n/a
    # Description:
    #     runs the main function, allows the user to select from a menu of functions

    while True:
        while True:
            choice = input("""
Recursive Menu
(1) Factorial
(2) Summation
(3) Exponentiation
(4) Fibonacci
(5) Digit Sum
(6) Digit Product
(7) Product (using recursion)
(8) Sum of numbers in a range
(9) Reverse Number
(0) Exit
                
Enter your choice:  """
            )
            if choice == 0:
                print("exited")
                return
            try:
                choice = abs(int(choice))
                print(f"Selected {choice}")
                break
            except ValueError:
                    print("pick a valid choice")

        
        while True: 
            try:
                number = abs(int(input("Please enter a positive integer to modify")))
                print(f"Entered {number}")
                break
            except ValueError:
                print("pick a valid integer")

        if choice == 1:
            print(f"Result: {factorial(number)}")

        elif choice == 2:
            print(f"Result: {summation(number)}")

        elif choice == 3:
            try:
                exponent = abs(int(input("Please enter a positive integer to serve as the exponent")))
                print(f"Entered {exponent}")
                print(f"Result: {exponention(number, exponent)}")
            except ValueError:
                print("pick a valid integer")
            

        elif choice == 4:
            print(f"Result: {fibonacci(number)}")

        elif choice == 5:
            print(f"Result: {digitsum(number)}")

        elif choice == 6:
            print(f"Result: {digitprod(number)}")

        elif choice == 7:
            try:
                second = abs(int(input("Please enter a positive integer to multiply")))
                print(f"Entered {second}")
                print(f"Result: {product(number, second)}")
            except ValueError:
                print("pick a valid integer")

        elif choice == 8:
            try:
                start = abs(int(input("Enter starting number: ")))
                if start <= number:
                    print(f"Entered {start}")
                    print(f"Result: {rangedsum(number, start)}")
                else:
                    print("pick a smaller starting number")
            except ValueError:
                print("pick a valid integer")

        elif choice == 9:
            print(f"Result: {reversednumber(number)}")



        else:
            print("Invalid input")
            
main()

