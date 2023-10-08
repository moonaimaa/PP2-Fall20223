n = int(input())  # Максимальное число
k = set(range(1, n + 1))  # Создаем множество всех возможных чисел от 1 до n

while True:
    a = input()  # Вопрос Беатрисы
    if a == "HELP":
        break  # Если получен ответ HELP, завершаем ввод
    
    answer = input()  # Ответ Августа
    a_set = set(map(int, a.split()))  # Преобразуем строку во множество чисел
    
    if answer == "YES":
        k &= a_set  # Пересечение множеств
    else:
        k -= a_set  # Разность множеств

result = sorted(k)  # Сортируем результат в порядке возрастания
print(" ".join(map(str, result)))  # Выводим числа через пробел
