

def get_book_text(filepath):
    
    with open(filepath) as file:
        book = file.read()
    
    return book

def count_words(string):
    array = string.split()
    noWords = len(array)
    return noWords





def main():

    bookString = get_book_text("./books/frankenstein.txt")
    #print(bookString)
    noWords = count_words(bookString)
    print(f"Found {noWords} total words")

main()