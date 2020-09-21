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

# DEBAG1
#print(np.where(cost_matrix == 9.5)[0])

#словарь отфильтрованных элементов
restricted = dict()

#сортировка по ресурсу и времени
for i in range(dim1):
  control_cost = min(cost_matrix[i])
  print(control_cost)
  j_find = np.where(cost_matrix == control_cost)[1]
  control_time = time_matrix[i][j_find]
  print(control_time)
  for j in range(dim2):
    print(cost_matrix[i][j])
    print(time_matrix[i][j])
    if ((control_cost <= cost_matrix[i][j]) and (control_time < time_matrix[i][j])):
      restricted.update({(i, j) : False})

# DEBAG2
#print(restricted.keys())

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
      control_time = time_matrix[i][j]
      break
  #пробег по элементам
  for j in range(np.shape(time_matrix)[1]):
    if j == control_j_counter:
      j += 1