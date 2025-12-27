
from stats import count_words, return_characters
import sys

def get_book_text(filepath):
    
    with open(filepath) as file:
        book = file.read()
    
    return book

def generate_report(filepath, noWords, SL):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {noWords} total words")
    print("--------- Character Count -------")
    for i in range(0, len(SL)):
        print(f"{SL[i][1]}: {SL[i][0]}")

def dictionary_sort(D):
    L = []
    for i in D:
        L.append((D[i], i))

    SL = sorted(L, reverse=True)

    return SL
  

def main():
    
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    #filepath = 'books/frankenstein.txt'

    bookString = get_book_text(filepath)
    #print(bookString)
    noWords = count_words(bookString)
    

    D = return_characters(bookString)
    

    SL = dictionary_sort(D)
    generate_report(filepath, noWords, SL)

try:
    main()
except Exception as e:
    print(e)