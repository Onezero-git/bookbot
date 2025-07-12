from stats import (
    count_words,
    count_letters,
    sorted_dicts,
    get_book_text
)


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    counted_letters = count_letters(text)
    list_of_dict = sorted_dicts(counted_letters)


    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    
    # Character Count output with only alphabetical letters
    print ("--------- Character Count -------")
    for i in range (0, len(list_of_dict)):
        if list_of_dict[i]["char"].isalpha() == True:
            print (f"{list_of_dict[i]["char"]}: {list_of_dict[i]["num"]}")
    print ("============= END ===============")


main()