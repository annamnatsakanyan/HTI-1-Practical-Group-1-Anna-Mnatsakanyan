word = input("enter the word: ").split()


def is_uppercase(word):
    word_uppercase = True
    for i in range(len(word)):
        if word[i] != word[i].upper():
            word_uppercase = False
            break
    return word_uppercase


if is_uppercase(word):
    print("Yes")
else:
    print("No")
