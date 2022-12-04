if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_value_arr = student_marks.get(query_name)
    avg = sum(query_value_arr)/len(query_value_arr)
    print("%.2f" % avg)
