def count_words(book):
    return len(book.split())

def count_letters(text):
    text = text.lower()
    result = {}
    for i in text:
        if i  in result:
            result[i] += 1
        else:
            result[i] = 1
    
    return result