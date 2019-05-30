"""
    6603 : 로또
    URL : https://www.acmicpc.net/problem/6603
    Input :
        7 1 2 3 4 5 6 7
        8 1 2 3 5 8 13 21 34
        0
    Output :
        1 2 3 4 5 6
        1 2 3 4 5 7
        1 2 3 4 6 7
        1 2 3 5 6 7
        1 2 4 5 6 7
        1 3 4 5 6 7
        2 3 4 5 6 7

        1 2 3 5 8 13
        1 2 3 5 8 21
        1 2 3 5 8 34
        1 2 3 5 13 21
        1 2 3 5 13 34
        1 2 3 5 21 34
        1 2 3 8 13 21
        1 2 3 8 13 34
        1 2 3 8 21 34
        1 2 3 13 21 34
        1 2 5 8 13 21
        1 2 5 8 13 34
        1 2 5 8 21 34
        1 2 5 13 21 34
        1 2 8 13 21 34
        1 3 5 8 13 21
        1 3 5 8 13 34
        1 3 5 8 21 34
        1 3 5 13 21 34
        1 3 8 13 21 34
        1 5 8 13 21 34
        2 3 5 8 13 21
        2 3 5 8 13 34
        2 3 5 8 21 34
        2 3 5 13 21 34
        2 3 8 13 21 34
        2 5 8 13 21 34
        3 5 8 13 21 34
"""

from itertools import combinations


first = True

while True:
    inp = list(map(int, input().split()))
    k = inp[0]
    if k == 0:
        break

    if not first:
        print()
    else:
        first = False

    s = inp[1:]
    for p in combinations(s, 6):
        print(' '.join([str(i) for i in p]))
