"""
Program to calculate ln(1-x) using power series expansion.
Lab Work 3, Variant 4
Version: 1.0
Developer: Ganiev Abubakr
Group: 453505
Date: 2026-03-28
"""

import math
from typing import Callable, Tuple, Generator

# ----------------------------
# Contains functions for sequence initialization
# ----------------------------

def sequence_generator(n: int) -> Generator[int, None, None]:
    """
    Generator that yields numbers from 0 to n-1.
    
    Args:
        n: Upper limit (exclusive)
        
    Yields:
        int: Numbers from 0 to n-1
    """
    for i in range(n):
        yield i

def initialize_with_generator(sequence: list) -> list:
    """
    Initialize sequence using a generator.
    
    Args:
        sequence: Empty list to be filled
        
    Returns:
        list: Initialized sequence
    """
    n = len(sequence)
    sequence[:] = list(sequence_generator(n))
    return sequence

def initialize_with_user_input(sequence: list) -> list:
    """
    Initialize sequence with user input.
    
    Args:
        sequence: Empty list to be filled
        
    Returns:
        list: Initialized sequence
    """
    for i in range(len(sequence)):
        while True:
            try:
                sequence[i] = float(input(f"Enter element {i+1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return sequence

# ----------------------------
# Contains custom decorators
# ----------------------------

def input_validator(func: Callable) -> Callable:
    """
    Decorator to validate input for ln_1_minus_x function.
    Ensures x is within valid range (-1 < x < 1).
    """
    def wrapper(x: float, eps: float) -> Tuple[float, int, float, float, float]:
        if not -1 < x < 1:
            raise ValueError("x must be in the range (-1, 1)")
        return func(x, eps)
    return wrapper

# ----------------------------
# Contains main calculation functions
# ----------------------------

def term_generator(x: float, max_terms: int = 500) -> Generator[float, None, None]:
    """
    Generator that yields terms of the series for ln(1-x).
    
    Args:
        x: Argument of the function
        max_terms: Maximum number of terms to generate
        
    Yields:
        float: Terms of the series (-x^n / n)
    """
    for n in range(1, max_terms + 1):
        yield -(x ** n) / n

@input_validator
def ln_1_minus_x(x: float, eps: float) -> Tuple[float, int, float, float, float]:
    """
    Calculate ln(1-x) using power series expansion.
    
    Args:
        x: Argument of the function (-1 < x < 1)
        eps: Precision of calculation
        
    Returns:
        Tuple: (result, terms_used, math_result, eps, x)
        
    Raises:
        ValueError: If maximum iterations (500) reached without convergence
    """
    result = 0.0
    math_result = math.log(1 - x)
    
    for n, term in enumerate(term_generator(x), 1):
        result += term
        if abs(term) < eps:
            return (result, n, math_result, eps, x)
    
    raise ValueError(f"Maximum iterations (500) reached without achieving precision {eps}")

# ----------------------------
# Contains user interface functions
# ----------------------------

def display_results_table(results: Tuple[float, int, float, float, float]) -> None:
    """
    Display results in a formatted table.
    
    Args:
        results: Tuple containing (result, terms_used, math_result, eps, x)
    """
    result, n, math_result, eps, x = results
    
    print("\nResults:")
    print("+-----------+-----------+-----------+-----------+-----------+")
    print("|     x     |     n     |   F(x)    | Math F(x) |    eps    |")
    print("+-----------+-----------+-----------+-----------+-----------+")
    print(f"| {x:9.6f} | {n:9d} | {result:9.6f} | {math_result:9.6f} | {eps:9.6f} |")
    print("+-----------+-----------+-----------+-----------+-----------+")

def get_float_input(prompt: str, min_val: float = None, max_val: float = None) -> float:
    """
    Get validated float input from user.
    
    Args:
        prompt: Message to display
        min_val: Minimum allowed value (optional)
        max_val: Maximum allowed value (optional)
        
    Returns:
        float: Validated user input
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value <= min_val:
                print(f"Value must be greater than {min_val}")
                continue
            if max_val is not None and value >= max_val:
                print(f"Value must be less than {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_yes_no_input(prompt: str) -> bool:
    """
    Get yes/no input from user.
    
    Args:
        prompt: Message to display
        
    Returns:
        bool: True for 'yes', False for 'no'
    """
    while True:
        response = input(prompt).lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        print("Please enter 'yes' or 'no'")

# ----------------------------
# Main program
# ----------------------------

def main():
    print("Program to calculate ln(1-x) using power series expansion")
    print("Developer: Ganiev Abubakr")
    print("Group: 453505")
    print("Variant: 4")
    print("Version: 1.0")
    print("Date: 2026-03-28\n")
    
    while True:
        try:
            x = get_float_input("Enter x value (-1 < x < 1): ", -1, 1)
            eps = get_float_input("Enter precision (eps > 0): ", 0)
            
            results = ln_1_minus_x(x, eps)
            display_results_table(results)
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        if not get_yes_no_input("\nDo you want to calculate another value? (yes/no): "):
            break

if __name__ == "__main__":
    main()