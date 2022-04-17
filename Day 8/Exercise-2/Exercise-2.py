# Write your code below this line 👇
def prime_checker(number):
    if number == 1:
        print("It\'s not a prime number.")
    elif number == 2:
        print("It\'s a prime number.")
    else:
        is_prime = True
        for checker in range(2, number):
            if number % checker == 0:
                is_prime = False
        if is_prime == True:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)