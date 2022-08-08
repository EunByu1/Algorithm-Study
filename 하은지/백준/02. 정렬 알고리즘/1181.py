# [0] sys 모듈 import 
import sys

# [1] 입력 및 중복 제거 
N     = int(sys.stdin.readline())
Word  = []

for i in range(N):
    Word.append(input())

Word = list(set(Word))

# [2] 중첩 정렬
#      : 첫 번째 정렬을 통해 알파벳 순으로 먼저 정렬된 후 
#        두 번째 정렬을 통해 길이 순으로 재정렬 됨
Word.sort()
Word.sort(key = len)

# [3] 출력
for i in Word:
    print(i)
