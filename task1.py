eagle = 0
tails = 0
coint = [1, 0, 1, 1, 1, 0]
count = 0
for i in range(len(coint)):
    if (coint[i] == 0):
        eagle += 1
    elif (coint[i] == 1):
        tails += 1
print(f"Решка {tails}")
print(f"Орел {eagle}")

if eagle > tails:
    count = tails
else:
    count = eagle
print(f"Нужно перевернуть {count} монеты")