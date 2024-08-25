PLACEHOLDER = "[name]"
with open('./src/mail/Input/Names/invited_names.txt', mode='r') as names_file:
    names = names_file.readlines()


with open('./src/mail/Input/letters/starting_letter.txt', mode="r") as letter_template:
    letter = letter_template.read()
    for name in names:
        new_letter = letter.replace(PLACEHOLDER, name.strip())
        with open(f'./src/mail/output/readyToSend/letter_for_{name.strip()}.txt', mode="w") as completed_letter:
            completed_letter.write(new_letter)







