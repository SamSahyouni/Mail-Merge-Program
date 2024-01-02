#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
for num in range(8):
#Replace the [name] placeholder with the actual name.
    with open("./Input/Names/invited_names.txt", mode="r") as file:
        lines = file.readlines()
        start_name = lines[num]
        name = start_name.strip()
    with open("./Input/Letters/starting_letter.txt", mode="r") as template:
        letter = template.read().replace("[name]", f"{name}")
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
            new_letter.write(letter)


    
