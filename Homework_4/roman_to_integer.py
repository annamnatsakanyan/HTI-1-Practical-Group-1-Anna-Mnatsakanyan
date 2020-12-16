roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_integer(number):
    i = 0
    product = 0
    while i < len(number):
        first_num = roman_nums[number[i]]
        if i + 1 < len(number):
            second_num = roman_nums[number[i + 1]]
            if first_num >= second_num:
                product += first_num
                i += 1
            else:
                product -= first_num
                i += 1
        else:
            product += first_num
            i += 1
    return product


numbers = input("enter a number: ").upper()
print(roman_to_integer(numbers))
