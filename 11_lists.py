if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        name, *line = input().split()
        value = list(map(int, line))

        if name == "append":
           arr.append(value[0])
        
        elif name == "insert":
            index,data = value[0],value[1]
            arr.insert(index,data)

        elif name == "print":
            print(arr)        

        elif name == "reverse":
            arr.reverse()

        elif name == "sort":
            arr.sort()

        elif name == "pop":
            arr.pop()
        
        elif name == "remove":
            data = value[0]
            arr.remove(data)