a = int(input())
b = []
k = []
if 1 <= a <= 10**5:
    for i in range(a):
        c = int(input())
        b.append(c)

for i in range(1, max(b)+1):
    for j in range(1, a+1):
        k.append(i)

    if sum(k) > sum(b):
        print(i)
        break
    else:
        k.clear()
