import pandas as pd

# TODO 1. Create a dictionary in this format:
df = pd.read_csv('nato_phonetic_alphabet.csv')
letter_word = {value.letter: value.code for (number, value) in df.iterrows()}
print(letter_word)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    word = input('Hello, whats you word? ').upper()
    answer = []
    for letter in word:
        answer.append(letter_word[letter])
    print(answer)
