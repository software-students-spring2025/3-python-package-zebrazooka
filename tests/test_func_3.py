import pytest
import random
import re
from artificial_unintelligence.function_3 import generate_sentence, load_word_bank

word_bank = load_word_bank()

def test_valid_letter():
    """Test if a randomly selected valid letter generates a proper sentence."""
    letter = random.choice(list(word_bank.keys()))  # Pick a random valid letter
    sentence = generate_sentence(letter)

    assert isinstance(sentence, str)  # Ensure output is a string
    assert len(sentence) > 0  # Ensure output is not empty
    assert sentence[-1] == '.'  # Ensure sentence ends with a period

def test_invalid_letter():
    """Test if an invalid letter raises a ValueError."""
    letter = 'ñ'  # Invalid letter
    with pytest.raises(ValueError, match=f"You provided an unsupported letter '{letter}'"):
        generate_sentence(letter)

def test_all_words_start_with_letter():
    """Test if all words in the generated sentence start with the given letter."""
    letter = random.choice(list(word_bank.keys()))  # Pick a random valid letter
    sentence = generate_sentence(letter)

    words = re.findall(r'\b\w+\b', sentence.lower())  # Extract words from sentence
    words = [word.strip(".,!?") for word in words]  # Remove punctuation

    for word in words:
        assert word.startswith(letter), f"Word '{word}' does not start with '{letter}'"