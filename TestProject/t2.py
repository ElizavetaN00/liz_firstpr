# 2
def square_from_digit():
    digit1 = float(input("Enter digit: "))
    square = digit1 ** 2
    return f"Square of digit {digit1} is {square}"

def even_odd_digit():
    digit2 = int(input("Enter digit: "))
    if digit2 % 2 == 0:
        print(f"Digit {digit2} is even")
    else:
        print(f"Digit {digit2} is odd")

print(square_from_digit())
even_odd_digit()