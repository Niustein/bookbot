def main():
    #with open("books/frakenstein.txt") as f:
    #    file_contents = f.read()
    #    num_words = len(file_contents.split())
        #print(file_contents)

    book_path = "books/frakenstein.txt"

    text_book = get_text(book_path)
    num_words = count_Words(text_book)
    dict_letters = count_letters(text_book)
#    print (dict_letters)
    list_sorted_letters = sort_dict(dict_letters)
#    print(list_sorted_letters)
#    print(len(list_sorted_letters))

    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document")
    
    for i in range(len(list_sorted_letters)):
        print (f"The {list_sorted_letters[i][0]} character was found {list_sorted_letters[i][1]} times")
    print(f"--- End Report ---")

def get_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()


def count_Words(text_book):
    return len(text_book.split())

def count_letters(text_book):
    dict_letters = {}
    for i in range(len(text_book)):
        if text_book[i].isalpha() and text_book[i].lower() not in dict_letters:
            dict_letters[text_book[i].lower()] = 1
        elif text_book[i].isalpha() and text_book[i].lower() in dict_letters:
            dict_letters[text_book[i].lower()] += 1  
    return dict_letters

def sort_dict(dictionary):
    return sorted(dictionary.items(), key=lambda dict: dict[1], reverse=True)

#used lambda notation instead
#def sort_by_value(dict):
#    return dict[1]

main()