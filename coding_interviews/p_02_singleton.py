# See also: https://python-patterns.guide/gang-of-four/singleton/
import threading
import time
from functools import wraps


class Singleton1:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
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
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton3RaceCondition(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            time.sleep(1)
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton4(type):
    lock = threading.Lock()
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls.lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
