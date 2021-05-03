# generating name.
# check if name has comtains number, if yes then quit

def name(first,last):
    for character in first:
        if character.isdigit():
            raise Exception("Your first name cannot contain any numbers!")
    for character in last:
        if character.isdigit():
            raise Exception("Your last name cannot contain any numbers!") 
    return first + " " + last