def solution(text: str) -> str:
    modified_list = []
    for i in text:
        if i == "#":
            if modified_list:
                modified_list.pop()
        else:
            modified_list.append(i)
    return ''.join(modified_list)


assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""


def solution2(candle_number: int, make_new: int) -> int:
    burned_candles = candle_number
    left_for_new_candles = candle_number

    while left_for_new_candles >= make_new:
        new_candles = left_for_new_candles // make_new
        burned_candles += new_candles
        left_for_new_candles = left_for_new_candles % make_new + new_candles

    return burned_candles


assert solution2(5, 2) == 9
assert solution2(1, 2) == 1
assert solution2(15, 5) == 18
assert solution2(12, 2) == 23
assert solution2(6, 4) == 7
assert solution2(13, 5) == 16
assert solution2(2, 3) == 2


def solution3(text: str) -> str:
    if not text:
        return ""
    final_list = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            final_list.append(text[i - 1])
            if count > 1:
                final_list.append(str(count))
            count = 1

    final_list.append(text[-1])
    if count > 1:
        final_list.append(str(count))

    return ''.join(final_list)


print(solution3("cccxbbaaa"))
print(solution3("aaa"))
assert solution3("cccbbaa") == "c3b2a2"
assert solution3("cccbba") == "c3b2a"
assert solution3("abeehhhhhccced") == "abe2h5c3ed"
assert solution3("aaabbceedd") == "a3b2ce2d2"
assert solution3("abcde") == "abcde"
assert solution3("aaabbdefffff") == "a3b2def5"
assert solution3("") == ""

