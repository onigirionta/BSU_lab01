import numpy as np

# столбец варианта
a = np.array([7.5, 8, 8.5, 9, 9.5])

# столбцы матрицы затрат
b_c = np.array([7, 8, 9, 10, 5])
c_c = np.array([2, 1, 6, 7, 3])
d_c = np.array([2, 3, 2, 1, 1])

# столбцы матрицы времени
b_t = np.array([3, 6, 7, 8, 9])
c_t = np.array([2, 5, 6, 7, 8])
d_t = np.array([9, 10, 11, 12, 5])

#составление матриц затрат и времени
c_matrix = np.transpose(np.array([a, b_c, c_c, d_c]))
t_matrix = np.transpose(np.array([a, b_t, c_t, d_t]))

dim1 = np.shape(c_matrix)[0]
dim2 = np.shape(c_matrix)[1]
t_border = 20.0

# DEBAG1
#print(np.where(c_matrix == 9.5)[0])

#словарь отфильтрованных элементов
restricted = dict()

#сортировка по ресурсу и времени
for i in range(dim1):
  control_c = min(c_matrix[i])
  print(control_c)
  j_find = np.where(c_matrix == control_c)[1]
  control_t = t_matrix[i][j_find]
  print(control_t)
  for j in range(dim2):
    print(c_matrix[i][j])
    print(t_matrix[i][j])
    if ((control_c <= c_matrix[i][j]) and (control_t < t_matrix[i][j])):
      restricted.update({(i, j) : False})

# DEBAG2
#print(restricted.keys())

#сортировка по времени
for i in range(dim1):
  control_summ_t = 0
  
  #очень тупая проверка
  for j in range(dim1):
    add = min(t_matrix[j])
    control_summ_t += add
    coord = np.where(t_matrix == add)
  if control_summ_t > t_border:
    print(f'Оптимальное решение в данном случае: t = {control_summ_t}, что больше максимального порога времени')
    quit()
  #отбор неотсортированного ближайшего элемента внутри строки
  for j in range(dim2):
    if (i, j) in restricted.keys():
      control_j_counter += 1
      pass
    else:
      control_t = t_matrix[i][j]
      break
  #пробег по элементам
  for j in range(np.shape(t_matrix)[1]):
    if j == control_j_counter:
      j += 1