"""
This mini-program analyzes names to make the generator more realistic by
looking at existing names and drawing conclusions.
"""
from main import VOWELS, CONSONANTS, grade_name


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


def get_detailed_analysis():
    """Get a detailed analysis based on the analysis methods in this
    file as to not call multiple methods."""
    # get the average name lengths
    get_average_name_length()
    print("\n")

    # get the most common start types (vowel or consonant)
    get_common_start_type()
    print("\n")

    # rank each letter by frequency
    rank_letters_by_popularity()
    print("\n")


def get_average_name_length():
    """Get the average length of a name."""
    lengths = dict()

    for name in NAMES:
        # get the length of the name
        name_length = len(name)
        
        # if the length isn't already in lengths
        if not name_length in lengths:
            # set it to zero
            lengths[name_length] = 0
        
        # regardless, increment the name length by 1
        lengths[name_length] += 1
    
    # get how many names are in names.txt
    names_length = len(NAMES)
    
    # sort lengths for better data presentation
    lengths_items = lengths.items()
    sorted_lengths = sorted(lengths_items)

    for length, times in sorted_lengths:
        # get the probability value
        probability = round((times / names_length) * 100, 2)

        # if the probability is greater than 1%
        if probability > 1:
            # print the probability for how frequent that length is
            print(f"{length} letters: {probability}%")


def get_common_start_type():
    """Returns the probability that the name starts with either a vowel or
    consonant."""
    # in the beginning, the number of vowels and consonants are zero
    n_vowels, n_consonants = 0, 0

    for name in NAMES:
        # get the lowercase version of the first letter in the name
        start_letter = name[0].lower()

        # if the start_letter is a vowel...
        if start_letter in VOWELS:
            # increment n_vowels by 1
            n_vowels += 1
        # otherwise, start_letter is a consonant
        else:
            # increment n_consonants by 1
            n_consonants += 1
    
    # get how many names are in names.txt
    names_length = len(NAMES)

    # get the probability values for vowels and consonants, respectively
    probability_vowel = round((n_vowels / names_length) * 100, 2)
    probability_consonant = round((n_consonants / names_length) * 100, 2)

    # print out results
    print(f"Start with vowel: {probability_vowel}%")
    print(f"Start with consonant: {probability_consonant}%")


def rank_letters_by_popularity():
    """Returns all letters ranked by how often they would be chosen."""
    letters = dict()

    for name in NAMES:
        # break up the name into letters
        for letter in name:
            # if a valid letter (vowel or consonat)...
            if letter in VOWELS or letter in CONSONANTS:
                # if the letter isn't already in letters
                if not letter in letters:
                    # set it to zero
                    letters[letter] = 0

                # regardless, increment by one
                letters[letter] += 1
    
    # get how many names are in names.txt
    names_length = len(NAMES)

    # sort letters for better data presentation
    letters_items = letters.items()
    sorted_letters = sorted(letters_items)

    for letter, freq in sorted_letters:
        # get the letter probability
        probability = round((freq / names_length) * 100, 1)

        # print out result
        print(f'"{letter}": {probability},')


def grade_all_names():
    """For every name in the names.txt file, grade it based on the grade_name
    method implemented in main.py."""
    for name in NAMES:
        # get the grade and print it out
        grade = grade_name(name)
        print(grade)


get_detailed_analysis()