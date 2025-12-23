

def get_book_text(filepath):
    
    with open(filepath) as file:
        book = file.read()
    
    return book







def main():

    bookString = get_book_text("./books/frankenstein.txt")
    print(bookString)
    

main()