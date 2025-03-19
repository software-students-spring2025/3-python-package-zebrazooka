import random
import json
import os

with open("word_bank.json", "r", encoding="utf-8") as input:
    try:
        word_bank = json.load(input)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in '{input}'.")

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

    if key not in word_bank:
        raise ValueError(f"You provided an unsupported letter '{start_letter}'. Available letters are: {list(word_bank.keys())}")

    noun = random.choice(word_bank[key]['nouns'])
    adjective = random.choice(word_bank[key]['adjectives'])
    verb = random.choice(word_bank[key]['verbs'])
    adverb = random.choice(word_bank[key]['adverbs'])

    sentence_template = random.choice(sentence_structures)
    sentence = sentence_template.format(noun=noun, adjective=adjective, verb=verb, adverb=adverb)

    return sentence.capitalize()
