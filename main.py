

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
    #print(characterDict)
    


def main():
    book_path = "./books/frankenstein.txt"
    book = import_file_contents(book_path)
    #print(book)
    word_count = wordCount(book)
    print(f"there are {word_count} words in this document")

    characterProcess(book)

main()
