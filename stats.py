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

def sort_on(items):
    return items["num"]

def sorted_dicts(dict):
    list_dict = []
    for i in dict:
        dict_to_list = {}
        dict_to_list["char"] = i
        dict_to_list["num"] = dict[i]
        list_dict.append(dict_to_list)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict