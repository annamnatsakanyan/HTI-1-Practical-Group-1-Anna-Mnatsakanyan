word = input("enter a string: ").lower()
reverse_word = word[::-1]
if word == reverse_word:
    print("Yes")
else:
    print("No")
