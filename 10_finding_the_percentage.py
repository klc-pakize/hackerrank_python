if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    for i in student_marks:
        if query_name == i:
            print("{:.2f}".format(sum(student_marks.get(i)) /len(student_marks.get(i))))

