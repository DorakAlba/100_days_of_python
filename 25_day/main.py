# TODO: Create a letter using starting_letter.txt

def open_letter():
    with open('./Input/Letters/starting_letter.txt') as g:
        return g.readlines()


def name_list():
    with open('./Input/Names/invited_names.txt') as n:
        return n.readlines()


def write_letter(name, template):
    name = name.strip()
    template[0] = template[0].replace('[name]', name)
    send = ''
    for line in template:
        send += (line)
    return send


template = open_letter()
names = name_list()
for name in names:
    letter = write_letter(name, template)
    print(name)
    with open(f'./Output/ReadyToSend/_{name.strip()}_letter.txt', mode='w') as file_letter:
        file_letter.write(letter)
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
