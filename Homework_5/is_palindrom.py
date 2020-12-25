def is_palindrom(text):
    if len(text) < 1:
        return True
    if text[0] == text[-1]:
        return is_palindrom(text[1:- 1])
    return False


text_input = input("enter some text: ")
if is_palindrom(text_input):
    print("Yes")
else:
    print("No")
