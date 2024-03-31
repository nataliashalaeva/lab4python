#Вариант 4 ЕГЭ-2023.
with open('27-167b.txt') as f:
    n, k = map(int, f.readline().split())
    data = [int(i) for i in f]
    min1 = min2 = min3 = 10 ** 100
    for i in range(k * 2, n):
        min1 = min(min1, data[i - k * 2])
        min2 = min(min2, data[i - k] * min1)
        min3 = min(min3, data[i] * min2)
print(min3 % (10 ** 6 + 1))
