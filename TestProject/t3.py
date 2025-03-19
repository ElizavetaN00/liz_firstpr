def summ_to_number(number):
    total_sum = 0

    for i in range(1, number + 1):
        total_sum += i

    return total_sum


print(summ_to_number(1))
print(summ_to_number(2))
print(summ_to_number(8))
print(summ_to_number(22))
print(summ_to_number(100))
