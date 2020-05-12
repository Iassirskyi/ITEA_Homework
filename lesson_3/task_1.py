import time


def decorator(func):

    start_time = time.time()

    def wrapper(*args, **kwargs):
        for _ in range(5000):
            result = func(*args, **kwargs)
        end_time = time.time()
        prog_time = end_time - start_time
        print(f'Program time: {prog_time} seconds ')
        return result

    return  wrapper


@decorator
def my_sum(a, b):
    return a + b
print(my_sum(51354982324, 455688321546879831))


@decorator
def some_func(a, b, c):
    return a**b - c**c

print(some_func(20, 50, 40))