#same as the __main__ file rn (which can also be used for testing) but that may change in the future 

from artificial_unintelligence.functions import get_random_word, random_sentence_reply, same_start_letter_generate

def main():
    print("Welcome to Artificial Unintelligence Demo!")
    print("\n1. Random Word Generator:")
    print(f"Random noun: {get_random_word('noun')}")
    print(f"Random verb: {get_random_word('verb')}")
    print(f"Random adjective: {get_random_word('adjective')}")
    
    print("\n2. Random Sentence Reply:")
    print(f"Random sentence: {random_sentence_reply()}")
    
    print("\n3. Random Sentence made of word start with same letter:")
    letter = input(f"give me a random letter: ")
    print(f"Random Sentence made of word start with " + letter + ": " + same_start_letter_generate(letter))

    print("\n4. Function 4")
 

if __name__ == "__main__":
    main()