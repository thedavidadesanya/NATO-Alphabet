import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}


usr_input = input("Enter a word: ").upper()
my_list = [phonetic_dict[letter] for letter in usr_input]

print(my_list)
