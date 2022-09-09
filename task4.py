growth_students = [165, 163, 160, 160, 157, 155, 154]
x = 162
print(growth_students)
for i in range(len(growth_students)):
    if growth_students[i] < x:
        print(f'Ученик в классе {i + 1} по росту')
        break

growth_students.insert(2, x)
print(growth_students)