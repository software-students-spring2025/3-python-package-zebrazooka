import artificial_unintelligence

from artificial_unintelligence.functions import get_random_word, random_sentence_reply, same_start_letter_generate, keyboard_smash

def main():
    print("Welcome to Artificial Unintelligence Demo!")
    print("\n1. Random Word Generator:")
    print(f"Random noun: {get_random_word('noun')}")
    print(f"Random verb: {get_random_word('verb')}")
    print(f"Random adjective: {get_random_word('adjective')}")
    
    print("\n2. Random Sentence Reply:")
    print(f"Random sentence: {random_sentence_reply('what is your opinion on the state of world affairs')}")
    
    print("\n3. Random Sentence made of word start with same letter:")
    letter = input(f"give me a random letter: ")
    print(f"Random Sentence made of word start with " + letter + ": " + same_start_letter_generate(letter))

    print("\n4. Function 4")
    keyboard_smash_text = input(f"input random letters ")
    print(f"Random Sentence with letters starting with keyboard smash" + keyboard_smash_text + " " + keyboard_smash(keyboard_smash_text))
 

if __name__ == "__main__":
    main()