def add_one_to_digits(digits):
    length_of_digits_list = len(digits)

    for i in range(length_of_digits_list - 1, -1, -1 ):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits


print(add_one_to_digits([9]))
print(add_one_to_digits([1,2,3]))
print(add_one_to_digits([1,1,9]))
print(add_one_to_digits([9,9,9]))
