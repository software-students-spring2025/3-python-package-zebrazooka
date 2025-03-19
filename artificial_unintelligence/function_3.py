import random
import json
import os

def load_word_bank(filename = "artificial_unintelligence/word_bank.json"):
    """This function helps to load the word bank json file that Jason put in"""
    with open(filename) as file: 
        return json.load(file)

def generate_sentence(start_letter: str) -> str:
    """
    Generates a sentence where all words start with the given letter.

    Parameters:
        start_letter (str): The letter that all words in the sentence should start with.

    Returns:
        str: A generated sentence following a random sentence structure.

    Raises:
        ValueError: If the given letter is not available in the word bank.

    Example:
        >>> generate_sentence('b')
        'Beautiful banana bounces briskly.'
    """

    sentence_structures = [
        "{adjective} {noun} {verb} {adverb}.",
        "{adjective} {noun} {verb} {adjective} {noun} {adverb}.",
        "{noun} {verb} {adverb} {adjective} {noun}.",
        "{adjective} {noun} {adverb} {verb} {adjective} {noun}.",
        "{noun} {adverb} {verb} {adjective} {noun}."
    ]

    key = start_letter.lower()
    word_bank = load_word_bank()

    if key not in word_bank:
        raise ValueError(f"You provided an unsupported letter '{start_letter}'. Available letters are: {list(word_bank.keys())}")

    noun = random.choice(word_bank[key]['nouns'])
    adjective = random.choice(word_bank[key]['adjectives'])
    verb = random.choice(word_bank[key]['verbs'])
    adverb = random.choice(word_bank[key]['adverbs'])

    sentence_template = random.choice(sentence_structures)
    sentence = sentence_template.format(noun=noun, adjective=adjective, verb=verb, adverb=adverb)

    return sentence.capitalize()

# Function 4: Keyboard smash

def keyboard_smash(smash: str) -> str: 
    word_data = load_word_bank()

    words = []

    for letter in smash.lower():
        if letter in word_data:
            word_bank = word_data[letter]
            noun = random.choice(word_bank.get('nouns', [letter]))
            adj = random.choice(word_bank.get('adjectives', [letter]))
            verb = random.choice(word_bank.get('verbs', [letter]))
            adverb = random.choice(word_bank.get('adverbs', [letter]))

            sentence_structure = random.choice([
                f"{adj} {noun} {verb} {adverb}.",
                f"{noun} {verb} {adverb} {adj} {noun}.",
                f"{adj} {noun} {adverb} {verb} {adj} {noun}."
            ])

            words.append(sentence_structure)
        else:
            words.append(letter)

        
    return " ".join(words)