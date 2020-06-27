"""
Jou, Artifical Name Generator
Brehanu Bugg, 06/26/2020
CSN Side Project

This program creates realistically-sounding names just for fun by creating
small vowel-consonant pairs and adding them together by following simple
rules as to not create names that sound too weird.
"""
from random import choice, randint, random
from termcolor import colored
from time import sleep


# create a list holding vowels and consonants, respectively
VOWELS = ["a", "e", "i", "o", "u"]
CONSONANTS = [chr(x) for x in range(97, 123) if chr(x) not in VOWELS]

# limits how many times the computer can randomly select from a list
SUBSET_LIMIT = 12

# the number of names to generate
N_NAMES = 18_000

# number of generated numbers
N_GENERATED = 0

# given analysis, this table contains how likely a letter would be after tested
# on 18,000+ names
MAPPED_LETTERS = {
    "a": 80.4,
    "b": 6.7,
    "c": 7.0,
    "d": 14.2,
    "e": 78.2,
    "f": 1.5,
    "g": 4.3,
    "h": 12.7,
    "i": 59.3,
    "j": 0.5,
    "k": 2.6,
    "l": 45.6,
    "m": 7.5,
    "n": 52.3,
    "o": 21.2,
    "p": 1.7,
    "q": 0.6,
    "r": 38.8,
    "s": 17.5,
    "t": 24.1,
    "u": 7.7,
    "v": 3.5,
    "w": 0.8,
    "x": 0.9,
    "y": 18.5,
    "z": 1.4
}


def chose_by_probability(lst):
    """Given a list of letters, choose one based on the MAPPED_LETTERS
    dictionary to make the names more realistic."""
    available_options = list()

    for letter in lst:
        # get the probability value from the table (the likeliness...)
        lookup_value = MAPPED_LETTERS[letter]

        # that many times, add that letter to the pool (available_options)
        for _ in range(int(lookup_value)):
            available_options.append(letter)
    
    # return a random choice (weighted probability)
    return choice(available_options)


def create_syllable():
    """Create a vowel-consonant pair."""
    # simple (and popular) vowel-consonant syllable structures
    # (v for vowel, c for consonant)
    syllable_structures = [
        "cv",
        "vc",
        "cvc",
        "v",
        "c"
    ]

    # chose a random syllable structure
    structure = choice(syllable_structures)
    syllable = list()

    # loop through each "v" and "c" in the structure
    for pair_type in structure:
        # if the current type is a consonant
        if pair_type == "c":
            # get SUBSET_LIMIT amount of random consonants
            consonants = [choice(CONSONANTS) for _ in range(SUBSET_LIMIT)]
            # use weighted probability to chose the most likely letter
            chosen_consonant = chose_by_probability(consonants)

            # add letter to the syllable per the syllable structure
            syllable.append(chosen_consonant)
        # the current type is a vowel
        else:
            # get SUBSET_LIMIT amount of random vowels
            vowels = [choice(VOWELS) for _ in range(SUBSET_LIMIT)]
            # use weighted probability to chose the most likely letter
            chosen_vowel = chose_by_probability(vowels)

            # add letter to the syllable per the syllable structure
            syllable.append(chosen_vowel)
    
    # return the joined syllable
    return "".join(syllable)


def create_name(n_syllables):
    """Create a name given a number of syllables."""
    name = list()

    # given how many syllables, repeat n times
    for _ in range(n_syllables):
        # create a syllable and append to the name list
        generated_syllable = create_syllable()
        name.append(generated_syllable)
    
    # join the name (so it's one string)
    joined_name = "".join(name)

    # return the name, capitalizing the first letter
    return joined_name.capitalize()


def grade_name(name):
    """Given a name, grade how realistic it sounds."""
    # make a lowercase copy for accurate grading
    name_lower = name.lower()
    # get how many letters are in the name
    name_length = len(name)

    # get the sum of vowels and consonants
    n_vowels = sum([1 for x in name_lower if x in VOWELS])
    n_consonants = sum([1 for x in name_lower if x in CONSONANTS])

    # most names are 3-7 letters
    is_good_length = True if name_length <= 7 and name_length >= 3 else False

    # most names have at least 2 vowels
    has_two_vowels = True if n_vowels >= 2 else False

    # most names have more consonants than vowels
    has_more_consonants = True if n_consonants >= n_vowels else False

    # most names start with a consonant
    starts_with_consonant = True if name_lower[0] in CONSONANTS else False

    # gather all critieria into a list for easier grading
    criterias = [
        is_good_length, 
        has_two_vowels, 
        has_more_consonants,
        starts_with_consonant]

    # add 1 to the sum if the criteria is True
    criterias_sum = sum([1 for x in criterias if x])

    # get the numeric grade [(part / total) * 100] of the name
    grade = round((criterias_sum / len(criterias)) * 100, 2)

    return grade


if __name__ == "__main__":
    # will hold all generated name
    names = list()

    # for _ in range(N_NAMES):
    while N_GENERATED != N_NAMES:
        # create a name with either 2 or 3 syllables
        name = create_name(randint(2, 3))
        
        # if the name has a grade above 75%...
        if grade_name(name) >= 75:
            # consider it a generated name
            names.append(f"{name}\n")

            # increment the number generated
            N_GENERATED += 1
    
    # write N_NAMES names to the generated_names.txt
    with open("generated_names.txt", "w") as f:
        f.writelines(names)