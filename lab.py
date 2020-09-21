import numpy as np

# столбец варианта
a = np.array([7.5, 8, 8.5, 9, 9.5])

# столбцы матрицы затрат
b_cost = np.array([7, 8, 9, 10, 5])
c_cost = np.array([2, 1, 6, 7, 3])
d_cost = np.array([2, 3, 2, 1, 1])

# столбцы матрицы времени
b_time = np.array([3, 6, 7, 8, 9])
c_time = np.array([2, 5, 6, 7, 8])
d_time = np.array([9, 10, 11, 12, 5])

#составление матриц затрат и времени
cost_matrix = np.transpose(np.array([a, b_cost, c_cost, d_cost]))
time_matrix = np.transpose(np.array([a, b_time, c_time, d_time]))

dim1 = np.shape(cost_matrix)[0]
dim2 = np.shape(cost_matrix)[1]
time_border = 20.0

#DEBAG1
#print(np.where(cost_matrix == 9.5)[0])

#словарь отфильтрованных элементов
restricted = dict()

#сортировка по ресурсу и времени
#DEBAG2
print(f'Costs matrix:\n{cost_matrix}')
print(f'Times matrix:\n{time_matrix}')

for i in range(dim1):
  control_minimal_cost = min(cost_matrix[i])
  print(f'***control_minimal_cost = {control_minimal_cost}***')
  mid_term = np.where(cost_matrix == control_minimal_cost)
  j_find = mid_term[1][mid_term[0] == i][0]
  print(f"***j_find = {j_find}***")
  control_matching_time = time_matrix[i][j_find]
  print(f'***control_matching_time = {control_matching_time}***')
  for j in range(dim2):
    print(f'control cost elem = {cost_matrix[i][j]}')
    print(f'control time elem = {time_matrix[i][j]}')
    if ((control_minimal_cost <= cost_matrix[i][j]) and (control_matching_time < time_matrix[i][j])):
      restricted.update({(i, j) : False})

#DEBAG3
print(restricted)

#сортировка по времени
for i in range(dim1):
  control_summ_time = 0
  
  #очень тупая проверка
  for j in range(dim1):
    add = min(time_matrix[j])
    control_summ_time += add
    coord = np.where(time_matrix == add)
  if control_summ_time > time_border:
    print(f'Оптимальное решение в данном случае: t = {control_summ_time}, что больше максимального порога времени')
    quit()
  #отбор неотсортированного ближайшего элемента внутри строки
  for j in range(dim2):
    if (i, j) in restricted.keys():
      control_j_counter += 1
      pass
    else:
      control_matching_time = time_matrix[i][j]
      break
  #пробег по элементам
  for j in range(np.shape(time_matrix)[1]):
    if j == control_j_counter:
      j += 1