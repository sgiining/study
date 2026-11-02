A, B = map(int, input().split())

for i in range(21):
    if i == 0:
        a = A//B
        print(a, end='')
        print('.', end='')
    else:
        b = (A%B) * 10
        A = b
        c = A//B
        print(c, end='')
