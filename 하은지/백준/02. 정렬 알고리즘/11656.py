# [0] 입력 
S      = input()
S_list = []


# [1] 입력 값 응용 후 리스트의 요소로 append 
for i in range(len(S)):
    S_list.append(S[i:])

    
# [2] 중첩 정렬 
S_list.sort(key=len)
S_list.sort()


# [3] 출력 
for i in S_list:
    print(i)
