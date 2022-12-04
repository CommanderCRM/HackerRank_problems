# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
fields = input()
marks_sum = 0

Students = namedtuple('Students', fields)

for i in range(n):
    student = Students(*input().split())
    marks_sum += int(student.MARKS)

avg = marks_sum/n
print(round(avg, 2))
