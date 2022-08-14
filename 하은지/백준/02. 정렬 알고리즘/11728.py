# [방법 1] 
# ---------------------------------------------------------------------
# [0] 모듈 import
import sys
import itertools


# [1] 입력 
N, M     = map(int, sys.stdin.readline().split())
A        = []
B        = []
Result_1 = []
Result_2 = []
String = ""

A.append(list(map(int, sys.stdin.readline().split())))
B.append(list(map(int, sys.stdin.readline().split())))


# [2] 배열 A & B 합친 후 Result_1에 Binding
Result_1 = A + B


# [3] 2차원 형태의 리스트 요소 값을 1차원 형태로 변환 후 Result_2에 Binding
for i in Result_1:
    Result_2.extend(i)

    
# [4] 정렬 
Result_2.sort()


# [5] 출력 
for i in Result_2:
    print(i, end=" ")
# ---------------------------------------------------------------------



# [방법 2] 
# ---------------------------------------------------------------------
# [0] 모듈 import 
import sys
import itertools


# [1] 입력 
N, M  = map(int, sys.stdin.readline().split())
A     = list(map(int, sys.stdin.readline().split()))
B     = list(map(int, sys.stdin.readline().split()))


# [2] 배열 A & B 합친 후 Result에 Binding
Result = A + B


# [3] 정렬 
Result.sort()


# [4] 출력 
for i in Result:
    print(i, end=" ")   
# ---------------------------------------------------------------------
