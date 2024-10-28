### open a stated file in books dir.
#https://www.geeksforgeeks.org/print-the-content-of-a-txt-file-in-python/
#with open("./books/frankenstein.txt", 'r') as file:
#    file_content = file.read()
#    file.close()

#print(file_content)


def import_file_contents(path):
    try: 
        file = open(path, 'r')

    except Exception:
        print('Error in read_file_contents')

    else:
        return file.read()

    finally:
        file.close()

def wordCount(file):
    newline_stripped_file = file.replace("\n", " ")
    space_delimited = newline_stripped_file.split(" ")
    while('' in space_delimited):
        space_delimited.remove('')
    return len(space_delimited)


def main():
    book_path = "./books/frankenstein.txt"
    book = import_file_contents(book_path)
    #print(book)
    word_count = wordCount(book)
    print(f"there are {word_count} words in this document")

main()
