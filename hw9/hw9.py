def solution(sequence):
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            count +=1
        if count > 1:
                return False
        if i >= 2 and sequence[i] <= sequence[i - 2]:
                sequence[i] = sequence[i - 1]
        else:
                sequence[i - 1] = sequence[i]
    return True

assert solution([1, 2, 3]) # True
assert not solution([1, 2, 1, 2]) # False
assert not solution([1, 3, 2, 1]) # False
assert not solution([1, 2, 3, 4, 5, 3, 5, 6]) # False
assert not solution([40, 50, 60, 10, 20, 30]) # False

print('Successful1')

def solution2(n, f_number):

    opp_number = (f_number + n//2) % n
    return opp_number

assert solution2(10, 6) == 1
assert solution2(10, 2) == 7
assert solution2(10, 4) == 9

print('Successful2')

def solution3(number):
    number_of_card = str(number)
    if not number_of_card.isdigit() or number_of_card == "":
        return False
    number_of_card = number_of_card[::-1]
    sum = 0
    for i in range(len(number_of_card)):
        int_digit = int(number_of_card[i])
        if i % 2 == 1:
            int_digit *= 2
            if int_digit > 9:
                int_digit -= 9
        sum += int_digit

    return sum % 10 == 0

assert not solution3(4561261212345464) # False
assert solution3(4561261212345467) # True
assert not solution3("") # False
assert solution3(6011111111111117) # True

print('Successful3')
