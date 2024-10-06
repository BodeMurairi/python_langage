import pandas as pd

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dictionary = {row.letter:row.code for (index, row) in alphabet.iterrows()}

game_on = True

while game_on:
    word = input("Can you write a word?").upper()
    try:
        output_list = [alphabet_dictionary[letter] for letter in word]
        print(output_list)
        game_on = False
    except KeyError:
        print("Please! Enter a valid word.")