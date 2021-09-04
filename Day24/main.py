with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

with open ("Input/Names/invited_names.txt") as people:
    names = people.read()

names = names.split('\n')

for name in names:
    modified_content = content.replace("[name]", name)

    with open(f"Output/ReadyToSend/{name}.docx", "w") as ready_letter:
        ready_letter.write(modified_content)
