import pandas #import Pandas for DF

alfabet_df = pandas.read_csv("nato_phonetic_alphabet.csv") #import csv
#print(alfabet_df)
alfabet_df_dict = {row.letter : row.code for (index,row) in alfabet_df.iterrows()}

name = input("Please provide your name: ")
#name = "test"
name_letters = list(name.upper())
name_alfa = [alfabet_df_dict[letter] for letter in name_letters if letter in alfabet_df_dict]

print("Your translation is: ")
print(name_alfa)
