#  Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области
#  4 больше, чем количество нулевых элементов в четных столбцах в области 1, то поменять в В симметрично области
#  2 и 3 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
#  После чего вычисляется выражение: ((F*A)– (K * AT) . Выводятся по мере формирования А, F и все матричные
#  операции последовательно.

# B C    2
# E D  1   3
#        4


import random
import sys


def check_even(n):
    return n % 2 == 0


k = int(input('Введите число K: '))
n = input('Введите число N > 5: ')

try:
    n = int(n)
    while n < 6:
        n = int(input('Число должно быть больше пяти: '))
except ValueError:
    sys.exit('Введено не число. Программа завершена.')

main_table = []
for i in range(n):
    work_list = []

    for j in range(n):
        work_list.append(random.randint(-10, 10))
    main_table.append(work_list)
'''
n = 10
main_table = [[0] * 10] * 10
actual_a_table = main_table
'''
print('Матрица А')
print('\n'.join('\t'.join(map(str, row)) for row in main_table))

if n % 2 == 1:  # Избавление от нечетных столбцов
    skip_number = int(n / 2) - 1
    print(
        f'Так как количество столбцов и строк нечетно, строка и столбец под номерами {skip_number + 1} не будут включены'
        f' в подматрицы\n')
else:
    skip_number = n / 2


print('Подматрица C:')
sub_table_c = []
for i in range(len(main_table)):
    work_list = []
    if check_even(n):
        temp = skip_number - 0
    else:
        temp = skip_number + 1
    if i < temp:
        for j in range(len(main_table[i])):
            if check_even(n):
                if j < skip_number + 1:
                    work_list.append(main_table[i][j])
            else:
                if j < skip_number + 2:
                    work_list.append(main_table[i][j])
        sub_table_c.append(work_list)

print_table = []
for x in range(len(sub_table_c)):
    print_table = []
    for j in range(len(sub_table_c[x]) - 1):
        print_table.append(sub_table_c[x][j])
    print(print_table)

sub_table_e = []
for i in range(len(main_table)):
    work_list = []
    if check_even(n):
        temp = skip_number - 1
    else:
        temp = skip_number - 0
    if i > temp:
        for j in range(len(main_table[i])):
            if check_even(n):
                if j > skip_number - 1:
                    work_list.append(main_table[i][j])
            else:
                if j > skip_number - 0:
                    work_list.append(main_table[i][j])
        sub_table_e.append(work_list)


sub_table_d = []
for i in range(len(main_table)):
    work_list = []
    if check_even(n):
        temp = skip_number - 1
    else:
        temp = skip_number + 1
    if i > temp:
        for j in range(len(main_table[i])):
            if check_even(n):
                if j < skip_number + 1:
                    work_list.append(main_table[i][j])
            else:
                if j < skip_number + 1:
                    work_list.append(main_table[i][j])
        sub_table_d.append(work_list)

sub_table_b = []
for i in range(len(main_table)):
    work_list = []
    if check_even(n):
        temp = skip_number - 0
    else:
        temp = skip_number + 2
    if i < temp:
        for j in range(len(main_table[i])):
            if check_even(n):
                if j > skip_number - 1:
                    work_list.append(main_table[i][j])
            else:
                if j > skip_number + 1:
                    work_list.append(main_table[i][j])
        sub_table_b.append(work_list)


odd_tabs = []
for i in range(len(sub_table_c)):
    if i % 2 == 1 and i != len(sub_table_c):
        odd_tabs.append(i)

sub_center_index = int(len(sub_table_c) / 2)

# -------------------------------------------------
zero_odd_fourth_count = 0
for i in range(len(sub_table_c)):
    for j in range(len(sub_table_c)):
        if (i > j) and ((i + j + 1) > (n // 2)) and sub_table_c[i][j] == 0 and (j + 1) % 2 == 1:
            zero_odd_fourth_count += 1


zero_even_first_count = 0
for i in range(1, len(sub_table_c) // 2):
    for j in range(i):
        if (j + 1) % 2 == 0 and sub_table_c[i][j] == 0:
            zero_even_first_count += 1

for i in range(int(len(sub_table_c) // 2), len(sub_table_c)):
    for j in range(len(sub_table_c) - (i + 1)):
        if (j + 1) % 2 == 0 and sub_table_c[i][j] == 0:
            zero_even_first_count += 1
print(zero_even_first_count, zero_odd_fourth_count)

if zero_odd_fourth_count > zero_even_first_count:
    print('Количество нулей на нечетных местах в четвертой области БОЛЬШЕ, чем нулей на четных местах в первой области')
    print('Подматрица B:')
    for x in sub_table_b:
        print(x)

    print('Симметрично поменяем области 2 и 3 местами:')
    del_n = n // 2
    g = del_n - 1
    for i in range(0, del_n):
        for j in range(0 + i, del_n - i):
            sub_table_b[i][j], sub_table_b[g - j][g - i] = sub_table_b[g - j][g - i], sub_table_b[i][j]

    for x in sub_table_b:
        print(x)
else:
    print('Количество нулей на нечетных местах в четвертой области НЕ БОЛЬШЕ, чем нулей на четных местах в первой области')
    print('Подматрица E:')
    for x in sub_table_e:
        print(x)
    print('Меняем C и E местами.')
    sub_table_c, sub_table_e = sub_table_e, sub_table_c

print('Матрица D:')
for x in sub_table_d:
    print(x)

print('Матрица F:')
f_table_up = sub_table_b
f_table_bot = sub_table_d
for x in range(len(sub_table_c)):
    for i in range(len(sub_table_c[x])):
        f_table_up[x].append(sub_table_c[x][i])

for x in range(len(sub_table_e)):
    for i in range(len(sub_table_e[x])):
        f_table_bot[x].append(sub_table_e[x][i])

for i in f_table_bot:
    f_table_up.append(i)

for x in f_table_up:
    print(x)

table_a_transposed = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        table_a_transposed[i][j] = main_table[j][i]
print("Транспонированая матрица A:")
for x in table_a_transposed:
    print(x)

table_FA = [[0 for i in range(n)] for j in range(n)]
table_KAT = table_a_transposed
for i in range(n):
    for j in range(n):
        for k in range(n):
            table_FA[i][j] += f_table_up[i][k] * main_table[k][j]
print('Результат F*A:')
for x in table_FA:
    print(x)

for i in range(n):
    for j in range(n):
        table_KAT[i][j] *= k
print('Результат K*A^T:')
for x in table_KAT:
    print(x)

answer_table = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        answer_table[i][j] = table_FA[i][j] - table_KAT[i][j]
print("Результат F*A-K*A^T:")
for x in answer_table:
    print(x)
