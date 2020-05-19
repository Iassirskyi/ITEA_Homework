from threading import Thread


def my_decorator(name_threard, is_daemon):
    def inner_decorator(func):
        def wrapper(*args):
            t = Thread(target=func, name=name_threard, args=args, daemon=is_daemon)
            return t.start()
        return wrapper
    return inner_decorator


@my_decorator('My_thread', False)
def some_func(name):
    print(f'Hello {name}')

some_func('some name')









