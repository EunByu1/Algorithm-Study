# [0] sys모듈 import
import sys

# [1] 학생 수 입력 
n = int(sys.stdin.readline())
students = []

# [2] 다중 정렬 
for i in range(n):
    name, d, m, y = sys.stdin.readline().split()
    students.append([name, int(y), int(m), int(d)])

students = sorted(students, key = lambda x : (x[1], x[2]))

# [3] 출력
print(students[-1][0])
print(students[0][0])
