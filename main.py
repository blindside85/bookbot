import os

def get_book_list() -> list:
    book_list = []
    for book in os.listdir("books"): 
        book_list.append(book)
    return book_list

def get_book_text(book: str) -> str:
    with open(f"books/{book}") as book_text:
        book_contents = book_text.read()
        return book_contents

def count_book_words(book: str) -> int:
    word_list = get_book_text(book).split()
    return len(word_list)

def count_book_chars(book: str) -> dict:
    char_list = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for char in get_book_text(book):
        if char.lower() in char_list:
            char_list[char.lower()] += 1
    return char_list

def get_book_report(book) -> None:
    book_map = count_book_chars(book)
    print(f"\n--- Begin report of {book} ---")
    print(f"{count_book_words(book)} words found in the document\n")
    for char in book_map:
        char_count = book_map[char]
        print(f"The '{char}' character was found {char_count} times")
    print("--- End report ---")



def main() -> None:
    books = get_book_list()
    print("Which book would you like a report on?")
    for i in range(0, len(books)):
        print(f"[{i}] {books[i]}")
    choice = int(input("\nEnter the number for the book you want: "))
    
    get_book_report(books[choice])
    
main()
