# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
num_notuniq = {}
num_uniq = {}
for i, num in enumerate(src):
    if num in num_notuniq:
        continue
    elif num in num_uniq:
        num_notuniq[num] = None
        del num_uniq[num]
    else:
        num_uniq[num] = i

result = sorted(num_uniq, key=num_uniq.get)
print(result)
