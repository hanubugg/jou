"""
This program goes through the names.txt file and generates how likely a letter
will follow a subsequent letter in hopes of making the name generator sound
more natural.
"""
from random import choice


# the generated markov chain
CHAIN = dict()

# holds all (non-generated) names
NAMES = None


# open the names.txt file
with open("names.txt", "r") as f:
    # read the entire file as one string
    contents = f.read()

    # remove newline characters
    stripped = contents.rstrip()

    # split each name by a newline
    NAMES = stripped.split("\n")


def create_chain():
    """Create the markov chain by looping through the names and adding each
    letter and subsequent letter to its own object."""
    for word in NAMES:
        # get the index for the letter to get the next letter
        for letter_index in range(len(word) - 1):
            letter = word[letter_index]
            subsequent = word[letter_index + 1]
        
            # if the letter isn't in the root chain...
            if letter not in CHAIN:
                # set it to an empty dictionary
                CHAIN[letter] = dict()
            
            # if the subsequent letter not in the inner dictionary...
            if subsequent not in CHAIN[letter]:
                # create it and set to zero
                CHAIN[letter][subsequent] = 0
            
            # regardless, increment subsequent by one
            CHAIN[letter][subsequent] += 1


def create_probability_values():
    """Loop through the CHAIN and for each letter, replace the number of
    occurances to probability of being the letter's successor."""
    for letter, subsequents in CHAIN.items():
        # get the values of the inner dictionary
        subsequents_values = subsequents.values()

        # calculate the average
        avg = sum(subsequents_values) / len(subsequents_values)

        # for each inner letter, recalculate the probability given the average
        for sub_letter, sub_subsequent in subsequents.items():
            CHAIN[letter][sub_letter] = CHAIN[letter][sub_letter] / avg


def choose_from_chain(letter, next_choices):
    """Given a letter, return a subsequent letter by using weighted probability
    to realistically create a word/name."""
    # get the available options
    subsequents = CHAIN[letter]
    available_options = list()

    for letter, value in subsequents.items():
        # if and ONLY if the letter is in the next_choices list
        if letter in next_choices:
            # get the frequency value
            rounded_value = int(value * 100)

            # same idea as chose_by_probability()
            for _ in range(rounded_value):
                available_options.append(letter)
    
    # chose a random item (weighted probability)
    return choice(available_options)


def get_likeliness_of_subsequent(letter, subsequent):
    """Given a letter, return how likely the subsequent would follow it."""
    # if the letter doesn't exist in the ROOT chain or if the subsequent does
    # not exist in the inner chain given letter, return 0 (no chance)
    if letter not in CHAIN or subsequent not in CHAIN[letter]:
        return 0
    
    # otherwise return the probability already there
    return CHAIN[letter][subsequent]


# automatically create the chain
create_chain()

# generate the probability values
create_probability_values()