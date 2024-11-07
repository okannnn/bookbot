

def import_file_contents(path):
    try: 
        file = open(path, 'r')

    except Exception:
        print('Error in read_file_contents')

    else:
        return file.read()

    finally:
        file.close()

def wordCount(text):
    count = text.split()
    return len(count)

def characterProcess(text):
    characterDict = {}
    for i in text:
        j = i.lower()
        #print(j)
        if j in characterDict:
            update_value = characterDict[j] + 1
            characterDict.update({j:update_value})
            #print("updated")
        else:
            characterDict.update({j:1})
            #print("Value Added")
    return(characterDict)
   
def report(filepath, word_count_str, characterDict):
    title_String = f"--- Begin Report of {filepath}"
    print(title_String)
    print(word_count_str)

    dictKeys = []
    dictValues = []
    
    for i in characterDict:
        dictKeys.append(i)
        #print(i)
        dictValues.append(characterDict[i])
        #print(characterDict[i])
    
    dictValues.sort()
    sortedDictKeys = []
    for i in range(len(dictValues) -1, 0, -1):
        #print(dictValues)

        mydict = {'george': 16, 'amber': 19}
        sortedDictKeys.append(list(characterDict.keys())[list(characterDict.values()).index(dictValues[i])])
        #print(list(characterDict.keys())[list(characterDict.values()).index(dictValues[i])])
    dictValues.reverse()
    for i in range(len(dictValues)-1):
        print(f"The {sortedDictKeys[i]} character was found {dictValues[i]} times")

    print("End Report")

def strippedCharacterDict(character_dict):
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "!", "@", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ";", ":", "'", '"', "\\" "|", "<", ",", ".", "/", "?", "\n", " "]

    for i in range(0, len(list)):
        if list[i] in character_dict:
            character_dict.pop(list[i])
    
    return character_dict

def main():
    book_path = "books/frankenstein.txt"
    book = import_file_contents(book_path)
    #print(book)
    word_count = wordCount(book)
    word_count_str = f"there are {word_count} words in this document"

    characterDict = characterProcess(book)
    #print(characterDict)

    stripped_character_dict = strippedCharacterDict(characterDict)

    report(book_path, word_count_str, stripped_character_dict)

main()
