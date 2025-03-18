def modify(s, n):
    if n < 1:
        return ""
    result = []
    for i in range(n):
        result.append(s[i])
    for i in range(n - 2, -1, -1):
        result.append(s[i])
    return ''.join(result)


s = "abcdefghijklmnopqrstuvwxyz"
print(modify(s, 1))
print(modify(s, 2))
print(modify(s, 3))
print(modify(s, 4))