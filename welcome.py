# Git in action
from turtle import color

print('Hello world')
print('This time is different')


# This example is derived from stack overflow tutorial
# https://stackoverflow.com/questions/60418497/how-do-i-use-kwargs-in-python-3-class-init-function


def add_attribute(milage: int = 1000) -> None:
    print(f'This car has gone {milage}')


class NewCar:
    def __init__(self, colour: str = 'red', attr_name: int = None, attr_value: str = None, *args, **kwargs):
        self.attr_name = attr_name
        self.attr_val = attr_value
        self.__colour = colour  # objects' hidden attribute
        self.__dict__.update(args)  # not sure if it works since there is no key
        self.__dict__.update(kwargs)
