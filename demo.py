#same as the __main__ file rn (which can also be used for testing) but that may change in the future 

from artificial_unintelligence.functions import get_random_word, random_sentence_reply
#idk this doesn't work 
#from artificial_unintelligence.function_3 import function_3  # Assuming function_3 is imported from this module

def main():
    print("Welcome to Artificial Unintelligence Demo!")
    print("\n1. Random Word Generator:")
    print(f"Random noun: {get_random_word('noun')}")
    print(f"Random verb: {get_random_word('verb')}")
    print(f"Random adjective: {get_random_word('adjective')}")
    
    print("\n2. Random Sentence Reply:")
    print(f"Random sentence: {random_sentence_reply()}")
    
    print("\n3. Function 3")
  
    
    print("\n4. Function 4")
 

if __name__ == "__main__":
    main()