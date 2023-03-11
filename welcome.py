# Git in action
from turtle import color

print('Hello world')
print('This time is different')

# This example is derived from stack overflow tutorial
# https://stackoverflow.com/questions/60418497/how-do-i-use-kwargs-in-python-3-class-init-function


class NewCar:
    def __init__(self, colour, *args, **kwargs):
        self.colour = colour
        self.__dict__.update(kwargs)
