import pytest

from coding_interviews.p_02_singleton import Singleton1, singleton2, Singleton3


class Singleton1Child1(Singleton1):
    # problem: child class __init__() will always be invoked
    def __init__(self) -> None:
        super().__init__()
        print(
            f"class name: {self.__class__.__name__}. I will always be invoked, so this is not perfect singleton."
        )


class Singleton1Child2(Singleton1):
    def __init__(self) -> None:
        super().__init__()
        print(
            f"class name: {self.__class__.__name__}. I will always be invoked too, so this is not perfect singleton."
        )


class Singleton1BadChild3(Singleton1):
    def __new__(cls, *args, **kwargs):
        # problem: no super(), override parent class behavior
        return object.__new__(cls)


# problem: child class will raise exception
@singleton2
class Singleton2:
    pass


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


def test_singleton1():
    ins1 = Singleton1()
    ins2 = Singleton1()
    assert ins1 == ins2

    child_ins1 = Singleton1Child1()
    child_ins2 = Singleton1Child1()
    child_ins3 = Singleton1Child2()
    child_ins4 = Singleton1BadChild3()
    child_ins5 = Singleton1BadChild3()
    assert child_ins1 == child_ins2
    assert child_ins1 != child_ins3
    assert child_ins4 != child_ins5


def test_singleton2():
    ins1 = Singleton2()
    ins2 = Singleton2()
    assert ins1 == ins2

    with pytest.raises(
        TypeError, match=r"function\(\) argument 'code' must be code, not str"
    ):

        class Singleton2Child1(Singleton2):
            pass


def test_singleton3():
    ins1 = Singleton3UsingMetaclass()
    ins2 = Singleton3UsingMetaclass()
    assert ins1 == ins2

    child_ins1 = Singleton3Child1()
    child_ins2 = Singleton3Child1()
    child_ins3 = Singleton3Child2()
    assert child_ins1 == child_ins2
    assert child_ins1 != child_ins3


def test_singleton_race_condition():
    pass
