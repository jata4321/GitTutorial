# Git in action
from turtle import color

print('Hello world')
print('This time is different')


# This example is derived from stack overflow tutorial
# https://stackoverflow.com/questions/60418497/how-do-i-use-kwargs-in-python-3-class-init-function


class NewCar:
    def __init__(self, colour,  attr_name=None, attr_value=None, *args, **kwargs):
        self.attr_name = attr_name
        self.attr_val = attr_value
        self.__colour = colour  # objects' hidden attribute
        self.__dict__.update(args)
        self.__dict__.update(kwargs)

    def add_attribute(self):
        pass

