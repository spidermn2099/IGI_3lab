"""
Program to read integers from keyboard and count even numbers.
Termination condition: entering a number greater than 1000.
Lab Work 3, Variant 4
Version: 1.0
Developer: Ganiev Abubakr
Group: 453505
Date: 2026-03-28
"""

from typing import Callable

# ----------------------------
# Contains custom decorators
# ----------------------------

def input_validator(func: Callable) -> Callable:
    """
    Decorator to validate that user input is an integer.
    """
    def wrapper() -> int:
        while True:
            try:
                value = func()
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return wrapper

# ----------------------------
# Contains main processing functions
# ----------------------------

@input_validator
def read_integer() -> int:
    """
    Read an integer from the user.
    
    Returns:
        int: The integer entered by the user.
    """
    return int(input("Enter an integer: "))

def count_even_until_gt_1000() -> int:
    """
    Read integers repeatedly until a number > 1000 is entered.
    Count how many even numbers were entered (excluding the terminating number).
    
    Returns:
        int: Count of even numbers.
    """
    even_count = 0
    while True:
        num = read_integer()
        if num > 1000:
            break
        if num % 2 == 0:
            even_count += 1
    return even_count

# ----------------------------
# Contains user interface functions
# ----------------------------

def display_result(even_count: int) -> None:
    """
    Display the result.
    
    Args:
        even_count: Number of even numbers entered.
    """
    print(f"\nNumber of even numbers entered: {even_count}")

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
    print("Program: count even numbers until a number > 1000 is entered")
    print("Developer: Ganiev Abubakr")
    print("Group: 453505")
    print("Variant: 4")
    print("Version: 1.0")
    print("Date: 2026-03-28\n")
    
    while True:
        try:
            even_count = count_even_until_gt_1000()
            display_result(even_count)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        if not get_yes_no_input("\nRun again? (yes/no): "):
            break

if __name__ == "__main__":
    main()