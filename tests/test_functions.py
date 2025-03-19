# tests/test_functions.py
import pytest
import json
import os
import random
import re
from artificial_unintelligence.functions import get_random_word, load_word_bank, random_sentence_reply, same_start_letter_generate

class TestLoadWordBank:
    """tests that the word bank actually loads"""
    def test_default_word_bank_loads(self):
        """tests that the word bank actually loads"""
        result = load_word_bank()
        assert isinstance(result, dict)
        assert 'a' in result
        assert 'o' in result 
        assert 'nouns' in result['a']
        assert 'nouns' in result['o']
        assert 'adjectives' in result['a']
        assert 'adjectives' in result['o']
        assert 'verbs' in result['a']
        assert 'verbs' in result['o']
    

class TestRandomSentenceReply:
    """Tests the random reply functions"""

    def test_returns_string(self):
        """Tests if it in fact returns a string (random sentence)"""
        result = random_sentence_reply()
        assert isinstance(result, str)
    
    def test_sentence_formatting(self):
        """Tests if the returned string is formatted correctly into a sentence (first letter uppercase and ends in punctuation)"""
        result = random_sentence_reply()
        assert result[0].isupper()  # First letter should be uppercase
        assert result[-1] in [".", "!", "?"]  # Should end with valid punctuation
    
    def test_different_calls_return_different_results(self):
        """Tests that multiple calls return different random sentences"""
        resulttable = [random_sentence_reply() for _ in range(5)]
        assert len(set(resulttable)) > 1  # At least two should be different

    def test_valid_letter(self): # for function 3
        """Test if a randomly selected valid letter generates a proper sentence."""
        word_bank = load_word_bank()
        letter = random.choice(list(word_bank.keys()))  # Pick a random valid letter
        sentence = same_start_letter_generate(letter)

        assert isinstance(sentence, str)  # Ensure output is a string
        assert len(sentence) > 0  # Ensure output is not empty
        assert sentence[-1] == '.'  # Ensure sentence ends with a period

    def test_invalid_letter(self): # for function 3
        """Test if an invalid letter raises a ValueError."""
        letter = 'ñ'  # Invalid letter
        with pytest.raises(ValueError, match=f"You provided an unsupported letter '{letter}'"):
            same_start_letter_generate(letter)

    def test_all_words_start_with_letter(self): # for function 3
        """Test if all words in the generated sentence start with the given letter."""
        word_bank = load_word_bank()
        letter = random.choice(list(word_bank.keys()))  # Pick a random valid letter
        sentence = same_start_letter_generate(letter)

        words = re.findall(r'\b\w+\b', sentence.lower())  # Extract words from sentence
        words = [word.strip(".,!?") for word in words]  # Remove punctuation

        for word in words:
            assert word.startswith(letter), f"Word '{word}' does not start with '{letter}'"
