"""
Program to count whitespace characters in input text.
Lab Work 3, Variant 4
Version: 1.0
Developer: Ganiev Abubakr
Group: 453505
Date: 2026-03-28
"""

from typing import Callable

# ----------------------------
# Contains text analysis functions
# ----------------------------

def count_whitespaces(text: str) -> int:
    """
    Count all whitespace characters in text.
    
    Args:
        text: Input string to analyze
        
    Returns:
        int: Count of whitespace characters
    """
    whitespace_chars = {' ', '\t', '\n', '\r', '\v', '\f'}
    return sum(1 for char in text if char in whitespace_chars)

# ----------------------------
# Contains all UI-related functions
# ----------------------------

def input_validator(func: Callable) -> Callable:
    """
    Decorator to validate text input is not empty.
    """
    def wrapper():
        while True:
            result = func()
            if result.strip():
                return result
            print("Error: Text cannot be empty. Please try again.")
    return wrapper

@input_validator
def get_text_input() -> str:
    """
    Get multi-line text input from user.
    
    Returns:
        str: Text entered by user
    """
    print("\nEnter your text (press Enter twice to finish):")
    lines = []
    while True:
        try:
            line = input()
            if line == '' and not lines:
                continue
            if line == '':
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def display_whitespace_count(text: str, count: int) -> None:
    """
    Display whitespace count results.
    
    Args:
        text: Analyzed text
        count: Number of whitespaces found
    """
    print("\nText analysis results:")
    print(f"Input text length: {len(text)} characters")
    print(f"Whitespace count: {count}")
    print(f"Text preview: {text[:50]}..." if len(text) > 50 else f"Text: {text}")

def ask_for_repeat() -> bool:
    """
    Ask user if they want to repeat analysis.
    
    Returns:
        bool: True if user wants to repeat, False otherwise
    """
    while True:
        answer = input("\nAnalyze another text? (y/n): ").lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'")

# ----------------------------
# Main program
# ----------------------------

def main():
    print("Program: count whitespace characters in a string")
    print("Developer: Ganiev Abubakr")
    print("Group: 453505")
    print("Variant: 4")
    print("Version: 1.0")
    print("Date: 2026-03-28\n")
    
    while True:
        try:
            text = get_text_input()
            whitespace_count = count_whitespaces(text)
            display_whitespace_count(text, whitespace_count)
            
            if not ask_for_repeat():
                break
                
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            if not ask_for_repeat():
                break

if __name__ == "__main__":
    main()