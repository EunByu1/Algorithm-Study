# [0] sys모듈 import
import sys

# [1] 학생 수 입력 및 변수 선언 
N        = int(sys.stdin.readline())
Students = []

# [2] 학생 정보 입력 및 다중 정렬
for i in range(N):
    name, k, e, m = sys.stdin.readline().split()
    Students.append([name, int(k), int(e), int(m)])

Students = sorted(Students, key = lambda x : (-x[1], x[2], -x[3], x[0]))

# [3] 출력
for i in range(N):
    print(Students[i][0])    
