def solve(s:str):
    if len(s) > 0 and 1000 > len(s):
        return ' '.join([i.capitalize() for i in s.split(" ")])

  

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
