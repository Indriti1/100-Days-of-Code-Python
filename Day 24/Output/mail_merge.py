PLACEHOLDER = "[name]"

with open("../Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("../Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip('\n')
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./ReadyToSend/letter_for_{stripped_name}.txt", mode="w+") as letter:
            letter.write(new_letter)

