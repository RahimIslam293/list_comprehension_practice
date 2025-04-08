import pandas #import Pandas for DF

alfabet_df = pandas.read_csv("nato_phonetic_alphabet.csv") #import csv
#print(alfabet_df)
alfabet_df_dict = {row.letter : row.code for (index,row) in alfabet_df.iterrows()}

def generate_phonetic():
    name = input("Please provide your name: ").upper()
    #name = "test"
    name_letters = list(name.upper())
    try:
        name_alfa = [alfabet_df_dict[letter] for letter in name]
    except KeyError:
        print("Please input a valid input.  Text only please.")
        generate_phonetic()
    else:
        print("Your translation is: ")
        print(name_alfa)
        invalid_input = False

generate_phonetic()
