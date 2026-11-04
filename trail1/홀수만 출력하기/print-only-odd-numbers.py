N = int(input())

i = 0
p = 0

while p < N:
    i = int(input())
    if i % 2 != 0 and i % 3 == 0:
        print(i)
    p += 1