from stats import count_words
from stats import count_letters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    print (f"{word_count} words found in the document")
    counted_letters = count_letters(text)
    print (counted_letters)


main()