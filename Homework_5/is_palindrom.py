def is_palindrom(text):
    if len(text) < 1:
        return "Yes"
    if text[0] == text[-1]:
        return is_palindrom(text[1:len(text) - 1])
    return "No"


text_input = input("enter some text: ")
print(is_palindrom(text_input))
