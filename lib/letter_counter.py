__author__ = 'alfons.lange'


def count_letters(string):
    obj = {}
    current_exists = False
    current_key = -1
    string = string.lower()

    for letter in string:
        current_exists = False
        current_key = -1

        if letter == " ":
            continue

        for key in obj:
            if key == letter:
                current_exists = True
                current_key = key

        if current_exists:
            obj[current_key] += 1
        else:
            obj[letter] = 1

    print obj
    return obj

count_letters("mississippihahaha")