import random
"""need to import random to get something random."""
import json 
import sys
import os

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

def load_word_bank(filename = "artificial_unintelligence/word_bank.json"):
    """This function takes in a file path (relative path works) and helps to load the word bank json file."""
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory of the script
    file_path = os.path.join(base_dir, "word_bank.json")  # Construct absolute path

    with open(file_path) as file:
        return json.load(file)

def random_sentence_reply(input_text=None):
    """This takes any text and just returns a randomly outputted sentence constructed from a sentence structure
    
    Parameters:
        input_text (str): This is any random query or sentence, or none at all. (It is randomly replied to so it doesn't affect the output)

    Returns:
        str: A randomly generated sentence of nouns, verbs, adjectives, and some special words. 


    Example:
        >>> random_sentence_reply("hi")
        'Sun were freely yawn fearless dragon but observe outstanding flower'
        """
    
    #got these based on sentences 
    sentence_structures = [
    ["adv", "adj", "n", "adv", "v", "adj", "n", "prep", "adj", "n"],
    ["n", "aux", "adv", "v", "adj", "n", "conj", "v", "adj", "n"],
    ["adv", "adj", "n", "v", "adv", "prep", "n", "prep", "adj", "n"],
    ["adj", "n", "aux", "v", "n", "adv", "conj", "adv", "v", "n"],
    ["interj", "n", "v", "adj", "n", "adv", "prep", "adj", "n"],
    ["adj", "n", "v", "adv", "prep", "adj", "n", "conj", "v", "n"],
    ["n", "aux", "adv", "v", "adj", "n", "rel", "v", "adj", "n"],
    ["adv", "n", "modal", "adv", "v", "n", "prep", "adj", "n", "prep", "n"],
    ["adj", "n", "adv", "v", "adj", "n", "conj", "adv", "v", "prep", "n"],
    ["n", "v", "n", "adv", "conj", "v", "adj", "n", "prep", "adj", "n"]
    ]

    special_words = {
            "prep": ["in", "on", "at", "by", "with", "from", "to", "for", "about"],
            "conj": ["and", "but", "or", "yet", "so", "because","when"],
            "aux": ["is", "are", "was", "were", "has", "have", "had"],
            "modal": ["can", "could", "will", "would", "shall", "should", "may", "must"],
            "rel": ["who", "whom", "whose", "that"],
            "interj": ["wow", "oh", "das crazy", "devastating", "ouch", "l+Ratio", "hmm", "well", "yay", "oops", "UWU"]
    }

    word_data = load_word_bank()
    
    sentence_struct = random.choice(sentence_structures)

    

    words = []
    for word_type in sentence_struct: 
        if word_type in special_words:
            words.append(random.choice(special_words[word_type]))
        else: 
            #correlate the two from the vategories in the word bank to the categories from the sentence struct lists provided above 
            json_key = {"n": "nouns", "v": "verbs", "adj": "adjectives", "adv":"adverbs"}.get(word_type, word_type)

            #note: don't refactor to use first function 
            random_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            #get the random word of the right category 
            word_options = word_data.get(random_letter,{}).get(json_key, [])

        
            #if like alphabetically you don't get one, could happen more with the special words 
            while not word_options:
                random_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
                word_options = word_data.get(random_letter,{}).get(json_key,[])            
            
            words.append(random.choice(word_options))

    #put spaces in between and make it uppercase and some puncuation so that it is a sentence 
    sentence = " ".join(words)
    sentence = sentence[0].upper() + sentence[1:] + str(random.choice([".","!","?"]))

    return sentence

# Function 3: sentence with same start letter for all words
def same_start_letter_generate(start_letter: str) -> str:
    """
    Generates a sentence where all words start with the given letter.

    Parameters:
        start_letter (str): The letter that all words in the sentence should start with.

    Returns:
        str: A generated sentence following a random sentence structure.

    Raises:
        ValueError: If the given letter is not available in the word bank.

    Example:
        >>> same_start_letter_generate('b')
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
    """ This function takes some random letters as the input and then in the ouput sends out a sentence with words starting with the letters in the input.
    
    Parameters:
        smash (str): A random series of letters. 

    Returns:
        str: A sequence of words that starts with the letters corresponding to the random sequence of letters in smash parameter. 


    Example:
        >>> keyboard_smash('ero')
        'Enthusiastically rainbow orange.'
    """
    word_data = load_word_bank()

    words = []

    for letter in smash.lower():
        if letter in word_data:
            word_bank = word_data[letter]
            word_choices = word_bank.get('nouns', []) + word_bank.get('adjectives', []) + \
                           word_bank.get('verbs', []) + word_bank.get('adverbs', [])
            if word_choices:
                chosen_word = random.choice(word_choices)
                words.append(chosen_word)
            else:
                words.append(letter)  # If no words available, just use the letter
        else:
            words.append(letter)  # If letter not in word bank, keep it as is
    
    sentence = " ".join(words).capitalize() + "."
    return sentence


