"""
Program to analyze text string with various operations.
Lab Work 3: Text Analysis, Variant 4
Version: 1.0
Developer: Ganiev Abubakr
Group: 453505
Date: 2026-03-28
"""

# ----------------------------
# Contains text analysis functions
# ----------------------------

def clean_word(word: str) -> str:
    """
    Clean word by removing trailing punctuation.
    
    Args:
        word: Input word to clean
        
    Returns:
        str: Cleaned word
    """
    while len(word) > 0 and word[-1] in {'.', ',', '!', '?', ';', ':'}:
        word = word[:-1]
    return word

def split_text(text: str) -> list:
    """
    Split text into words, handling commas and spaces as separators.
    
    Args:
        text: Input string to split
        
    Returns:
        list: List of cleaned words (lowercase, without punctuation)
    """
    words = text.replace(',', ' ').lower().split()
    return [clean_word(word) for word in words]

def count_short_words(words: list, max_length: int = 5) -> int:
    """
    Count words shorter than specified length.
    
    Args:
        words: List of words to analyze
        max_length: Maximum word length (exclusive)
        
    Returns:
        int: Count of short words
    """
    return sum(1 for word in words if len(word) < max_length)

def find_shortest_word_ending_with(words: list, ending: str) -> str:
    """
    Find shortest word ending with specified letter.
    
    Args:
        words: List of words to analyze
        ending: Letter the word should end with
        
    Returns:
        str: Found word or empty string if none found
    """
    ending_words = [word for word in words if word.endswith(ending)]
    if not ending_words:
        return ""
    return min(ending_words, key=len)

def sort_words_by_length(words: list, reverse: bool = True) -> list:
    """
    Sort words by their length.
    
    Args:
        words: List of words to sort
        reverse: Whether to sort in descending order
        
    Returns:
        list: Sorted list of words
    """
    return sorted(words, key=len, reverse=reverse)

# ----------------------------
# Contains all UI-related functions
# ----------------------------

def display_results(short_count: int, shortest_d_word: str, sorted_words: list) -> None:
    """
    Display analysis results in clear format.
    
    Args:
        short_count: Count of short words
        shortest_d_word: Shortest word ending with 'd'
        sorted_words: Words sorted by length
    """
    print("\nText Analysis Results:")
    print(f"a) Words shorter than 5 characters: {short_count}")
    
    print(f"\nb) Shortest word ending with 'd': ", end="")
    print(shortest_d_word if shortest_d_word else "No such word found")
    
    print("\nc) Words sorted by length:")
    for i, word in enumerate(sorted_words, 1):
        print(f"{i}. {word} (length: {len(word)})")

# ----------------------------
# Main program
# ----------------------------

def main():
    text = ("So she was considering in her own mind, as well as she could, for the hot day made "
            "her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would "
            "be worth the trouble of getting up and picking the daisies, when suddenly a White "
            "Rabbit with pink eyes ran close by her.")
    
    print("Program: text analysis (variant 4)")
    print("Developer: Ganiev Abubakr")
    print("Group: 453505")
    print("Variant: 4")
    print("Version: 1.0")
    print("Date: 2026-03-28\n")
    
    try:
        words = split_text(text)
        
        short_word_count = count_short_words(words)
        shortest_d = find_shortest_word_ending_with(words, 'd')
        sorted_by_length = sort_words_by_length(words)
        
        display_results(short_word_count, shortest_d, sorted_by_length)
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()