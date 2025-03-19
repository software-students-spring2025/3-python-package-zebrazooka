import random
"""need random to get something random"""
import json 

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
    """This function helps to load the word bank json file that Jason put in"""
    with open(filename) as file: 
        return json.load(file)

def random_sentence_reply(input_text=None):
    """This just returns a randomly outputted sentence constructed from a sentence structure"""
    
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

