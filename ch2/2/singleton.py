from functools import wraps


class Singleton1:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


def singleton2(cls):
    _instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrapper


class Singleton3(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton3, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
