def char_count(text):
    char_dict = {}
    for elements in text:
        keys = char_dict.keys()
        if elements in keys:
            char_dict[elements] += 1
        else:
            char_dict[elements] = 1
    return char_dict


text_input = input("enter a text: ")
print(char_count(text_input))
