# open starting_letter.txt file
import random
# open invited_names file
file = open("/home/bode/Documents/programming/100_days_ofCode/day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt")
invited_names = file.readlines()
# Choose Random names inside invited_names
choosen_names = random.choice(invited_names)

# open starting letter file
letter = open("/home/bode/Documents/programming/100_days_ofCode/day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt")
all_letter = letter.read()

# Convert list to string and replace the first line
mod_letter = ''.join(all_letter)
mod_letter = mod_letter.replace("[name],", choosen_names)
print(mod_letter)