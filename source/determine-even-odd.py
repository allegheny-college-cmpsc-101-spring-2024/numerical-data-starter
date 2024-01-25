# TODO: Make sure that you understand how this function
# uses modular arithmetic to perform a computation

# TODO: Make sure that you understand how this function
# uses type annotations to describe its input and output

# TODO: Make sure that you understand how this function
# uses conditional logic to make a decision

def determine_even_odd(value: int) -> str:
    """Determine if a number is even or odd."""
    # use modular arithmetic to determine if the number is even
    if value % 2 == 0:
        return "even"
    # since the number is not even, conclude that it is odd
    else:
        return "odd"

print("Determining whether integer values are even or odd")

# perform the computation with the value of zero
number = 0
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")


# perform the computation with the value of ten
number = 10
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")


# perform the computation with the value of eleven
number = 11
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")


# use a negative value for the computation
number = -10
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")


# use a negative value for the computation
number = -11
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")
