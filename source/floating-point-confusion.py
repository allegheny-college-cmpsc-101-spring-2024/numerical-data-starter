# TODO: Make sure that you understand each of the source
# code statements in the following function
#
# TODO: You should be able to explain when the result conforms
# to your expectations because of your knowledge of mathematics
# and when it diverges from your expectations
#
# TODO: Make sure that you can explain why the results diverge
# from your expectations in the situations when they do

def compute_one_by_addition() -> float:
    """Perform addition in a loop that is expected to add to 1.0."""
    # initialize the number to 0.0
    number = 0.0
    for _ in range(10):
        number = number + 0.1
    return number


def compute_one_by_multiplication() -> float:
    """Perform a multiplication that is expected to be 1.0."""
    multiply_number = 10.0 * 0.1
    return multiply_number


def floating_point_confusion_addition() -> str:
    """Demonstrate the properties of floating point numbers."""
    # call compute_one_by_addition and assign the return value into a variable called one_by_addition
    one_by_addition = compute_one_by_addition()
    # check to see if one_by_addition is equal to 1.0
    if one_by_addition == 1.0:
        message = f"After addition, the value of {one_by_addition} is equal to 1.0!"
    else:
        message = f"After addition, the value of {one_by_addition} is not equal to 1.0!"
    return message
    

def floating_point_confusion_multiplication() -> str:
    """Demonstrate the properties of floating point numbers."""
    # call compute_one_by_multiplication and assign the return value into a
    # variable called one_by_multiplication
    one_by_multiplication = compute_one_by_multiplication()
    # check to see if one_by_multiplication is equal to 1.0
    if one_by_multiplication == 1.0:
        message = f"After multiplication, the value of {one_by_multiplication}\
            is equal to 1.0!"
    else:
        message = f"After multiplication, the value of {one_by_multiplication}\
            is not equal to 1.0!"
    return message

def floating_point_confusion_comparison() -> str:
    """Compare the additive computation with the multiplicitive computation."""
    # call compute_one_by_addition and assign the return value into a
    # variable called one_by_addition
    one_by_addition = compute_one_by_addition()
    # call compute_one_by_multiplication and assign the return value into a
    # variable called one_by_multiplication
    one_by_multiplication = compute_one_by_multiplication()
    if one_by_addition == one_by_multiplication:
        message = f"The additive value of {one_by_addition} is equal to the\
            multiplicitive value of {one_by_multiplication}!"
    # the results are again not the same
    else:
        message = f"The additive value of {one_by_addition} is not equal to the\
            multiplicitive value of {one_by_multiplication}!"
    return message


# TODO: call the function that will illustrate some of the "strange" properties
# of using floating point numbers in Python.
print("Illustrating some strange properties of floating-point numbers!")

addition_message = floating_point_confusion_addition()
print(addition_message)

multiplication_message = floating_point_confusion_multiplication()
print(multiplication_message)

comparison_message = floating_point_confusion_comparison()
print(comparison_message)
