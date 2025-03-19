import pytest 
import sys
import os

# Add the parent directory to sys.path to resolve module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from artificial_unintelligence.functions import keyboard_smash

def test_keyboard_smash():
    
    test_input = "abc"
    result = keyboard_smash(test_input)

    print(f"Generated sentence: {result}")

    assert isinstance(result, str), "Output should be a string"
    assert len(result) > 0, "Result shouldn't be empty"

    words = result.split()
    assert words[0][0].lower() == "a", "First word should start with the letter a"
    assert words[1][0].lower() == "b", "Second word should start with b"
    assert words[2][0].lower() == "c", "Third word should start with c"

    assert result[-1] in [".", "!", "?"], "Output should end with punctuation"

if __name__ == "__main__":
    pytest.main()