def palindrome():
    data = input("Enter string or digit: ")
    low_no_s = ''.join(data.split()).lower()
    if low_no_s == low_no_s[::-1]:
        print(f"'{data}' is palindrome")
    else:
        print(f"'{data}' is non palindrome")


palindrome()