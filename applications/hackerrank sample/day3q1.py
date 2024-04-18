def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)

    st = n - mid
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# test_cases = int(input())
# for cs in range (test_cases):
#     n = int(input())
#     a = list(map(int, input().split()))
#     findZigZagSequence(a, n)

for n in range(7,11):
    findZigZagSequence(list(range(1,n+1)), n)

import math
