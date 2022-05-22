import random, string

givenStrings = ['abcd', 'abdc', 'ab32', 'Ab45']

def arrayContainsItem(item, array):
    for arrItem in array:
        if item == arrItem:
            return True
    return False

def generateRandomUniqueStrings(length, comparison):
    generatedString = ''.join(random.choices(string.ascii_letters+string.digits, k=length))
    check = arrayContainsItem(generatedString, comparison)
    while check == True:
        generatedString = ''.join(random.choices(string.ascii_letters+string.digits, k=length))
        check = arrayContainsItem(generatedString, comparison)

    return generatedString


print(generateRandomUniqueStrings(20, givenStrings))

