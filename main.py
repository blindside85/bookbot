def get_book_text() -> str:
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
        return book_contents

def count_book_words() -> int:
    word_list = get_book_text().split()
    return len(word_list)

def count_book_chars() -> dict:
    char_list = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for char in get_book_text():
        if char.lower() in char_list:
            char_list[char.lower()] += 1
    return char_list

def main() -> None:
    book_text = get_book_text()
    frank_char_map = count_book_chars()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_book_words()} words found in the document\n")
    for char in frank_char_map:
        char_count = frank_char_map[char]
        print(f"The '{char}' character was found {char_count} times")
    print("--- End report ---")

main()
