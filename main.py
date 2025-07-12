from stats import count_words
from stats import count_letters
from stats import sorted_dicts

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


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
        keys_list = list(list_of_dict[i].keys())
        if list_of_dict[i]["char"].isalpha() == True:
            print (f"{list_of_dict[i]["char"]}: {list_of_dict[i]["num"]}")
    print ("============= END ===============")


main()