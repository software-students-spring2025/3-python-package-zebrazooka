# tests/test_functions.py
import pytest
import json
import os
from artificial_unintelligence.functions import get_random_word, load_word_bank, random_sentence_reply, keyboard_smash

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
    """tests the random reply class"""

    def test_returns_string(self):
        """tests if it in fact returns a string (random sentence)"""
        result = random_sentence_reply()
        assert isinstance(result, str)
    
    def test_sentence_formatting(self):
        """tests if the returned string is formatted correctly into a sentence, first letter uppercase and ends in punctuation """
        result = random_sentence_reply()
        # Check if first letter is uppercase
        assert result[0].isupper()
        # Check if ends with punctuation
        assert result[-1] in [".", "!", "?"]
    
    def test_different_calls_return_different_results(self):
        """test that it's random and that multiple calls are working """
        
        resulttable = []
        counter = 1

        while counter <= 5:
            resulttable.append(random_sentence_reply())
            counter += 1
        
        
        # At least two of the five results should be different
        assert len({resulttable[0], resulttable[1], resulttable[2], resulttable[3], resulttable[4]}) > 1

