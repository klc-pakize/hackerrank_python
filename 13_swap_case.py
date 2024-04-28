def swap_case(s):
    sting=""
    for i in s:
        if i.isupper():
            character = i.lower()

        else:
            character = i.upper()
        sting += character

    return sting

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)