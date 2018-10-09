from collections import deque


def get_ugly_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    q2 = deque()
    q3 = deque()
    q5 = deque()

    q2.append(2)
    q3.append(3)
    q5.append(5)
    while n > 1:
        x = min(q2[0], q3[0], q5[0])
        if x == q2[0]:
            q2.popleft()
            q2.append(x * 2)
            q3.append(x * 3)
            q5.append(x * 5)
        elif x == q3[0]:
            q3.popleft()
            q3.append(x * 3)
            q5.append(x * 5)
        elif x == q5[0]:
            q5.popleft()
            q5.append(x * 5)

        n -= 1

    return x


print(get_ugly_number(1500))
