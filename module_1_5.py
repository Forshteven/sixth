immutable_var = 1, 2, 3, 'four', 5.5 #присвоить переменной кортеж из разных типов данных
print(immutable_var) #вывести кортеж на экран
immutable_var[1] = 10 #попытаться изменить элемент кортежа (невозможно, поскольку обращение к элементам кортежа не поддерживается)
mutable_list = [121, 144, 225] #присвоить переменной список из нескольких элементов
mutable_list[::] = 169, 196, 256 #изменить элементы списка
print(mutable_list) #вывести изменённый список на экран
