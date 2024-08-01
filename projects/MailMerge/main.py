#TODO: Create a letter using starting_letter.txt 
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as f:
            f.write(new_letter)