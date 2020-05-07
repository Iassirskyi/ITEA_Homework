from datetime import datetime


def decorator(func):

    start_time = datetime.now()

    def wrapper(*args, **kwargs):
        result = [func(*args, **kwargs) for _ in range(5)]
        print(result)
        end_time = datetime.now()
        prog_time = end_time - start_time
        print(f'Program time: {prog_time} seconds ')
        return result

    return  wrapper


@decorator
def my_sum(a, b):
    return a + b
my_sum(5000000000, 455688321546879831)

@decorator
def some_func(a, b, c):
    return a**b - c**c

some_func(20, 50, 40)

