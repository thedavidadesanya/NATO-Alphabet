import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():

    usr_input = input("Enter a word: ").upper()
    try:
        my_list = [phonetic_dict[letter] for letter in usr_input]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(my_list)

generate_phonetic()