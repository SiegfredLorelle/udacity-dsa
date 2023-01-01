"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    # Might as well be error, but the instruction said return 0 instead (others also consider 0 as the start of fibonacci seq)
    if position == 0:
        return 0
    # First two value in Fibonacci is 1 (cannot use formula)
    elif position == 1 or position == 2:
        return 1
    # If value is more than 2 then formula is applicable (Fn = Fn-2 + Fn-1)
    elif position > 2:
        value = get_fib(position - 2) + get_fib(position - 1)
        return value
    # Just incase an invalid integer is given
    else:
        return "ERROR: Cannot get the fibonacci value. Given position must be positive integer."
# Test cases
print(get_fib(9)) 
print(get_fib(11)) 
print(get_fib(0)) 
