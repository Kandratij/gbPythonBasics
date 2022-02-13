# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class DivByZero(ZeroDivisionError):
    pass


a, b = map(int, input('Input divide statement (example: a/b)').split('/'))
try:
    if b == 0:
        raise DivByZero('Divide by zero!!!')
    else:
        print(f'a/b={a/b}')
except DivByZero as ex:
    print(ex)



