#Функция вычисления чисел Фибоначчи
def fib(n):
    if n == 1 or n == 2:
        return 1
    return (fib(n-1) + fib(n-2))
print(fib(int(input())))


fib(0)
fib(1)
fib(9)
