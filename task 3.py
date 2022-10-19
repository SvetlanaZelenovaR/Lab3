objects = [['в', 3, 25],
           ['п', 2, 15],
           ['б', 2, 15],
           ['а', 2, 20],
           ['и', 1, 5],
           ['н', 1, 15],
           ['т', 3, 20],
           ['о', 1, 25],
           ['ф', 1, 15],
           ['д', 1, 10],
           ['к', 2, 20],
           ['р', 2, 20]]

# Находим элементы "Очки выживания / Ячейки" и сортируем их по убыванию

points_per_size = []
for i in range(len(objects)):
    points_per_size.append([objects[i][0], objects[i][1], objects[i][2], objects[i][2] / objects[i][1]])

points_per_size.sort(key = lambda j: j[3], reverse = True)

need = [], []       # Взятые предметы
all_points = 0      # Сумма всех очков выживания
good_points = 20    # Очки выживания взятых предметов
total = 0           # Итоговый счёт
k = 0
i = 0

for point in range(len(points_per_size)):
    all_points += points_per_size[point][2]

# Заполняем массив взятых элементов

while k < 8:
    indx = i
    i += 1
    if points_per_size[indx][1] == 1:
        need[0].append(points_per_size[indx][0])
        good_points += points_per_size[indx][2]
        k += points_per_size[indx][1]

    if points_per_size[indx][1] == 2:
        need[1].append(points_per_size[indx][0])
        need[1].append(points_per_size[indx][0])
        good_points += points_per_size[indx][2]
        k += points_per_size[indx][1]

# Выводим массив вязтых предметов

for row in need:
    for elem in row:
        print(elem, end = ' ')
    print()

print('Итоговые очки выживания:', good_points - (all_points - good_points))
