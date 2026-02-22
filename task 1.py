def factorial(num):
    '''User-defined function to find the factorial of a number
    :arg num: takes integer number to find its factorial
    :returns: the factorial of num'''

    factorial_num=1                          # Stores the factorial of the number
    while num>0:
        factorial_num=factorial_num*num
        num-=1
    return factorial_num                     # Returns the Factorial_num when calling

user_input=int(input("Enter a number to Finds its factorial: "))

print(f"The factorial of {user_input} is {factorial(user_input)}")  # printing the called factorial function
