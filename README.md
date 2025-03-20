# Python Package Exercise

# Artifical-Unintelligence 

[![Status](https://github.com/software-students-spring2025/3-python-package-zebrazooka/actions/workflows/build.yaml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-zebrazooka/actions/workflows/build.yaml)


## Our Project
Our project, artifical unintelligence, builds upon the rapidly growing AI/ML field. It is an evolution (but backwards) of AI/ML. By randomly generating dubiously  meaningful sentences, we can bring the field to the next level (maybe).

By: [Jonathan Gao](https://github.com/jg169), [Jason Mai](https://github.com/JasonMai233), [Nawab Mahmood](https://github.com/NawabMahmood), [dibukseid](https://github.com/dibukseid)

[Link to PyPI website for the proj](https://pypi.org/project/artificial-unintelligence/0.1.4/)


## How-To

[Demo Link](https://github.com/software-students-spring2025/3-python-package-zebrazooka/blob/main/demo.py) to example project. 


## Installation 

In terminal or console or bash, type 

```
pip install artificial-unintelligence
```

## Importing and Using 

In your project include

```python

import artificial_unintelligence

from artificial_unintelligence.functions import get_random_word, random_sentence_reply, same_start_letter_generate, keyboard_smash

```

### Functions 

#### Get a random word 

Use the get_random_word function. The parameters can be 'noun', 'verb', or 'adjective'. 

```python

#To get a random noun
random_noun = get_random_word('noun')
print(random_noun) 
#The output would look something like :'dog'

#To get a random verb
random_verb = get_random_word('verb')
print(random_noun)
#The output would look something like : 'jump' 

#To get a random adjective 
random_adjective = get_random_word('adjective')
print(random_adjectove)
#The output would look something like 'happy'

```

#### Generate a random sentence

Use the random_sentence function to unintelligently reply to a query that is inputted as an argument into the function. It takes any string as an argument. 

```python
#Reply to a query with a randomly generated sentence. 
random_sentence = random_sentence_reply('what do you think of fishes')
print(random_sentence)
# This output would be for example : "Quickly happy zebra loudly jumps scary car in big tree."
```

#### Generate Letter-Specific Sentences 



Use the same_start_letter_gemerate function to generate a sentence that all starts with the same letter. It takes an input as an argument or parameter. 

```python 

# To generate a sentence where the words start with e
e_sentence = same_start_letter_generate('e')
print(e_sentence)
#example output would be: Electric eels emulsify eaton
```

#### Keyboard Smash (for frustration)

Use the keyboard_smash function to create a sentence where the first letter matches with the letters of the keyboard smash. It takes a string as an argument or parameter. 

```python
#to convert a keyboard smash such as 'lkjae' 
smash_text = keyboard_smash("lkjae")
print(smash_text) 
#example output would be : light kind joeys after emus
```


### Set Up the virtual environment, install dependencies, build and test 

Clone the repository 

```
git clone https://github.com/software-students-spring2025/3-python-package-zebrazooka.git
```
   

To run, please first install pipenv in your console/terminal/bash. 

```
Pip install pipenv
```

Then go to the directory where the repo clone in your computer's terminal or console. 

Install the development environment and dependencies. --dev is important for pytest. 

```
pipenv install --dev
```

Install the package in development mode. If no edits would need to be made, then the -e can be removed. 

```
pipenv install -e . 
```

To install build 

```
pipenv install build
```

Generate distribution packages 
```
pipenv run python -m build
```


Run the demo and test using pipenv 

```
pipenv run python demo.py 
```

### If you would like to contribute (and how to test before you do)

Follow the steps to set Up the virtual environment, install dependencies, build and test , make sure to do the 'pipenv install -e .' command for easy editing. 

Then create a new branch 

```
git checkout -b newfeature
```

Make your updates

Run the tests 

```
pipenv run pytest
```

commit the changes

```
git commit -m 'some new feature'
```

Push to the branch

```
git push origin newfeature
```

Then go to github and open a pull request. We will look at it and the maintainer will update the PyPI project.


### How to import data 

Our github repo already comes ready with a word bank, with this structure: 

```JSON
"a": {
        "nouns": ["apple", "astronaut", "ant"],
        "adjectives": ["amazing", "angry", "awesome"],
        "verbs": ["arrive", "ask", "admire"],
        "adverbs": ["anxiously", "angrily", "awkwardly"]
    },
```

