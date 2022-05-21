# -*- coding: utf-8 -*-
"""baekjoon_1920.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n1mNFpk9QAN4XX0uD9TmINvB63h7Chqr
"""

num1 = int(input())
exp = list(map(int,input().split()))
num2 = int(input())
tar = list(map(int,input().split()))
exp.sort()
for k in tar:
    left, right = 0, len(exp) - 1
    is_find = False

    while True:
        median = (left + right) // 2
        if k == exp[median]:
            print(1)
            is_find = True
            break
        elif k > exp[median]:
            left = median + 1
        elif k < exp[median]:
            right = median - 1
        
        if left > right:
            break
    if not is_find:
        print(0)