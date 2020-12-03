word = input("enter the word: ").split()


def is_uppercase(uppercase_word):
    word_uppercase = True
    for i in range(len(uppercase_word)):
        if uppercase_word[i] != uppercase_word[i].upper():
            word_uppercase = False
            break
    return word_uppercase


if is_uppercase(word):
    print("Yes")
else:
    print("No")
