import random

def get_random_word(category: str) -> str:
    """
    Returns a random word from the specified category.
    
    Parameters:
        category (str): The category of the word. Supported values are 'noun', 'verb', and 'adjective'.
        
    Returns:
        str: A random word from the chosen category.
        
    Raises:
        ValueError: If an unsupported category is provided.
        
    Example:
        >>> get_random_word('noun')
        'dog'
    """
    words = {
        'noun': ['dog', 'cat', 'tree', 'car', 'bus'],
        'verb': ['run', 'jump', 'fly', 'swim', 'eat'],
        'adjective': ['happy', 'sad', 'bright', 'loud', 'scary']
    }
    
    key = category.lower()
    if key not in words:
        raise ValueError(f"You gave a unsupported category '{category}'. Supported categories are: {list(words.keys())}")
    
    return random.choice(words[key])
