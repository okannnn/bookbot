

def count_words(string):
    array = string.split()
    noWords = len(array)
    return noWords

def return_characters(string):
    lowerString = string.lower()
    Dict = {}

    for i in range(0, len(string)):
        if lowerString[i] in Dict:
            Dict[lowerString[i]] += 1
        else:
            Dict[lowerString[i]] = 1
        
    return Dict