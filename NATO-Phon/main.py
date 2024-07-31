import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phon_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def gen_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        list = [phon_dict[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        gen_phonetic()
    else:
        print(list)

gen_phonetic()