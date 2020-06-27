# Jou, Name Generator

A simple name generator by using patterns in existing names.

A simple side project by **[Brehanu Bugg](https://github.com/thebrehanubugg)**.

## Introduction

After waking up with the sudden urge to have my computer generate random names, I immediately opened up my computer and opened a new Python file, not knowing where exactly to start. *How do you get the computer to create something as complex as a name?* I started looking at popular names for example:

* Sofia

* Luke

* Emily

I realized every name is composed of syllables. Syllables themselves are composed of vowel/consonant pairs. Given that, I created a simple program to generate a name given a name structure of `consonant/vowel/consonant/vowel` and here were some examples:

1. Fola

2. Zewo

3. Higa

This was a start, but I wanted something more advanced. And that was when I started analyzing names using the power of Python.

## Name Analysis

In the repository, you'll see an `analysis.py` file. I used this to find patterns in a list of 18,000 names I downloaded from online. And this was some data I collected:

- Most names have 3-7 letters, the most common being 6 letters at 26.21%

- 86.21% of names start with a consonant

- Syllables could be 2 or 3 letters

Given that data, I quickly was able to create a table (which is `MAPPED_LETTERS` in `main.py`) of each letter, and how frequently they appeared in `names.txt`. I also created the function `chose_by_probability()` that used [weighted probability](http://www.columbia.edu/~md3405/BE_Risk_4_15.pdf) to return a letter using the `MAPPED_LETTERS` table.

Names appeared slightly better, but not quite what I wanted.

## Syllables

The biggest factor in a successful name is the syllable: the building block of a name. For this, I took a small subset of real names and analyzed them by hand. I noticed some recurring syllable structures:

- `consonant/vowel`

- `vowel/consonant`

- `consonant/vowel/consonant`

- `vowel`

- `consonant`

I modified the `make_syllable()` function to chose one of the above syllable structures and populate the syllable according to the structure. Depending on whether or not the next letter is a vowel or consonant, it randomly choses a `SUBSET_LIMIT` amount of them and then choses a random letter from that random list based on `chose_by_probability()` which uses weighted probability.

The names improved drastically, but I needed a way to filter out the names that weren't "good".

## The Grading System

Much like a search algorithm, my program only works as well as the parameters given. In the search algorithms, the better the heuristic, the better the search path. For this name generator program, I implemeted a `grade_name()` function based on important information gathered from `analysis.py`:

- Most names have 3-7 letters, the most common being 6 letters at 26.21%

- 86.21% of names start with a consonant

- Most names have at least 2 vowels

- Most names have more consonants than vowels

Taking in a name, the `grade_name()` function grades it based on the above criteria and returns a grade between 0-100. In the `__main__` function in `main.py`, it generates 18,000 names and weeds out the ones with a grade less than 75%. There are some noticable tweaks that could be made to better the algorithm:

* Increasing the "passing" grade from 75% to 90% (which comes at a risk for removing names that *are* good, but don't pass the grade requirement)

* Adding another criteria for grading the likeliness for each letter to follow the one before it in the name (this would require a Markov chain--which is implemented--but could remove the "computer touch" for the generated names)

* Counting how many syllables it has (this is not implemented but it would be interesting to see what it would consider a *good* syllable count)

## Results

This program generated some *interesting* names to say the least. Here are some of the most noticeable ones:

- Daniyal

- Assi

- Becaa

- Yale

- Yee

Suprisingly enough, this program randomly creates *real* names as well:

- Sam

- Michael

- Liz

- Iris

- Roy

And it created real words:

- Since

- Yes

- Lily

- Terra

- Rest

## Conclusion

Although the idea for the program proved to be a simple concept (create a name), the thinking and process behind it was interesting. It required me to find real names, analyze them (with the computer's help), and modifiying the algorithm based on new information I found.

And while this program is far from perfect, it does what I wanted. You can pronounce all the names. Some sound foreign, some sound cool, and some sound *very* similar to real names.