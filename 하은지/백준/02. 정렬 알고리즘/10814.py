# [0] sys 모듈 import
import sys

# [1] 입력
N = int(sys.stdin.readline())
List = []

for i in range(N):
    old, name = sys.stdin.readline().split()
    List.append([int(old), name])

# [2] 정렬
List.sort(key = lambda x : x[0])

# [3] 출력
for i in range(N):
    print(List[i][0], List[i][1])
