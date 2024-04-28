def count_substring(string, sub_string):
    sub_string_len = len(sub_string)
    cursor = 0
    count = 0

    for _ in string:
        if string[cursor:sub_string_len] == sub_string:
            count += 1
        cursor += 1
        sub_string_len += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# ABCDCDC
# CDC