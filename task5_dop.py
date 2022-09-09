from random import sample
n = int(input('Введите число кустов: '))
shrub = []
for i in range(n + 1):
    shrub = sample(range(0, 1000), n)
print(shrub)

max = 0
for i in range(1, len(shrub)-1):
    sum = shrub[i-1] + shrub[i] + shrub[i+1]
    if sum > max:
        max = sum
print(max)
