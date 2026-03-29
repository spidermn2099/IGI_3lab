"""
Program for processing real-valued lists with various operations.
Lab Work 3: List Processing, Variant 4
Version: 1.0
Developer: Ganiev Abubakr
Group: 453505
Date: 2026-03-28
"""

from typing import List, Tuple, Optional, Callable
import random

# ----------------------------
# Contains list initialization methods
# ----------------------------

def input_validator(func: Callable) -> Callable:
    """
    Decorator to validate list size input.
    Ensures size is positive integer.
    """
    def wrapper():
        while True:
            try:
                size = func()
                if size <= 0:
                    raise ValueError("Size must be positive")
                return size
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    return wrapper

@input_validator
def get_list_size() -> int:
    """
    Get valid list size from user.
    
    Returns:
        int: Validated list size
    """
    return int(input("Enter list size (positive integer): "))

def initialize_with_generator(size: int) -> List[float]:
    """
    Initialize list with random float values.
    
    Args:
        size: List size
        
    Returns:
        List[float]: Generated list
    """
    return [round(random.uniform(-10, 10), 2) for _ in range(size)]

def initialize_with_user_input(size: int) -> List[float]:
    """
    Initialize list with user input values.
    
    Args:
        size: List size
        
    Returns:
        List[float]: User-provided list
    """
    lst = []
    print(f"Enter {size} real numbers:")
    for i in range(size):
        while True:
            try:
                val = float(input(f"Element {i+1}: "))
                lst.append(val)
                break
            except ValueError:
                print("Invalid input. Please enter a real number.")
    return lst

# ----------------------------
# Contains list processing functions (variant 4)
# ----------------------------

def find_max_abs_index(lst: List[float]) -> int:
    """
    Find index of maximum absolute value element.
    
    Args:
        lst: Input list
        
    Returns:
        int: Index of max absolute element (0‑based)
    """
    return max(range(len(lst)), key=lambda i: abs(lst[i]))

def find_product_between_zeros(lst: List[float]) -> Tuple[Optional[float], str]:
    """
    Calculate product between first two zero elements.
    
    Args:
        lst: Input list
        
    Returns:
        Tuple: (product, message)
    """
    try:
        first_zero = lst.index(0)
        second_zero = lst.index(0, first_zero + 1)
        
        if second_zero - first_zero <= 1:
            return None, "No elements between zeros"
            
        product = 1.0
        for num in lst[first_zero+1:second_zero]:
            product *= num
        return product, "Success"
        
    except ValueError:
        return None, "Not enough zeros in list"

# ----------------------------
# Contains UI-related functions
# ----------------------------

def display_list(lst: List[float]) -> None:
    """
    Display list elements in readable format.
    
    Args:
        lst: List to display
    """
    print("\nCurrent list:")
    for i, val in enumerate(lst):
        print(f"{i+1}. {val:.2f}")

def display_results(lst: List[float], max_idx: int, product_result: Tuple[Optional[float], str]) -> None:
    """
    Display processing results.
    
    Args:
        lst: Processed list
        max_idx: Index of max absolute element
        product_result: Tuple of (product, message)
    """
    print("\nProcessing results:")
    print(f"- Index of max absolute element: {max_idx + 1} (value: {lst[max_idx]:.2f})")
    
    product, message = product_result
    if product is not None:
        print(f"- Product between zeros: {product:.4f}")
    else:
        print(f"- Product between zeros: {message}")

def get_menu_choice() -> int:
    """
    Get valid menu choice from user.
    
    Returns:
        int: User choice (1-3)
    """
    while True:
        print("\nMenu:")
        print("1. Generate random list")
        print("2. Enter list manually")
        print("3. Exit")
        
        try:
            choice = int(input("Your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            print("Please enter 1, 2 or 3")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_to_continue() -> bool:
    """
    Ask user if they want to continue.
    
    Returns:
        bool: True to continue, False to exit
    """
    while True:
        answer = input("\nContinue? (y/n): ").lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'")

# ----------------------------
# Main program
# ----------------------------

def main():
    print("Program: process list – max absolute index and product between zeros")
    print("Developer: Ganiev Abubakr")
    print("Group: 453505")
    print("Variant: 4")
    print("Version: 1.0")
    print("Date: 2026-03-28\n")
    
    while True:
        try:
            choice = get_menu_choice()
            
            if choice == 3:
                break
                
            size = get_list_size()
            
            if choice == 1:
                lst = initialize_with_generator(size)
            else:
                lst = initialize_with_user_input(size)
            
            display_list(lst)
            
            max_idx = find_max_abs_index(lst)
            product_result = find_product_between_zeros(lst)
            
            display_results(lst, max_idx, product_result)
            
            if not ask_to_continue():
                break
                
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            if not ask_to_continue():
                break

if __name__ == "__main__":
    main()