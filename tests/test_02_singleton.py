import concurrent
import time

import pytest

from coding_interviews.p_02_singleton import (
    Singleton1,
    Singleton3,
    Singleton3RaceCondition,
    Singleton4,
    singleton2,
)


class Singleton1Child1(Singleton1):
    # Problem: `__init__()` in child class will always be invoked.
    def __init__(self) -> None:
        super().__init__()
        print(
            f"class name: {self.__class__.__name__}. I will always be invoked, so this is not a perfect singleton."
        )


class Singleton1Child2(Singleton1):
    def __init__(self) -> None:
        super().__init__()
        print(
            f"class name: {self.__class__.__name__}. I will always be invoked too, so this is not a perfect singleton."
        )


class Singleton1BadChild3(Singleton1):
    def __new__(cls, *args, **kwargs):
        # Problem: no `super()`, override parent class behavior.
        return object.__new__(cls)


# Problem: child class will raise exception.
@singleton2
class Singleton2:
    pass


# "With a metaclass, it will only be called once, when the only instance is created."
# This is the best one except importing module.
# ref: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton3UsingMetaclass(metaclass=Singleton3):
    pass


class Singleton3Child1(Singleton3UsingMetaclass):
    def __init__(self) -> None:
        super().__init__()
        print(f"class name: {self.__class__.__name__}. I will only be invoked once.")


class Singleton3Child2(Singleton3UsingMetaclass):
    def __init__(self) -> None:
        super().__init__()
        print(
            f"class name: {self.__class__.__name__}. I will only be invoked once too."
        )


class Singleton3RaceConditionUsingMetaclass(metaclass=Singleton3RaceCondition):
    pass


class Singleton4UsingMetaclass(metaclass=Singleton4):
    pass


def test_singleton1():
    ins1 = Singleton1()
    ins2 = Singleton1()
    assert ins1 == ins2

    child_ins1 = Singleton1Child1()
    child_ins2 = Singleton1Child1()
    child_ins3 = Singleton1Child2()
    child_ins4 = Singleton1BadChild3()
    child_ins5 = Singleton1BadChild3()
    assert child_ins1 is child_ins2
    assert child_ins1 is not child_ins3
    assert child_ins4 is not child_ins5


def test_singleton2():
    ins1 = Singleton2()
    ins2 = Singleton2()
    assert ins1 is ins2

    with pytest.raises(
        TypeError, match=r"function\(\) argument 'code' must be code, not str"
    ):

        class Singleton2Child1(Singleton2):
            pass


def test_singleton3():
    ins1 = Singleton3UsingMetaclass()
    ins2 = Singleton3UsingMetaclass()
    assert ins1 is ins2

    child_ins1 = Singleton3Child1()
    child_ins2 = Singleton3Child1()
    child_ins3 = Singleton3Child2()
    assert child_ins1 is child_ins2
    assert child_ins1 is not child_ins3

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(Singleton3RaceConditionUsingMetaclass) for _ in range(2)]
    instances = [f.result() for f in futures]
    assert any(ins is not instances[0] for ins in instances)


def test_singleton4():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(Singleton4UsingMetaclass) for _ in range(2)]
    instances = [f.result() for f in futures]
    assert all(ins is instances[0] for ins in instances)
