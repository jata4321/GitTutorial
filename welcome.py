# Git in action
from turtle import color

print('Hello world')
print('This time is different')


class NewCar:
    def __init__(self, colour, *args, **kwargs):
        self.colour = colour
        self.__dict__.update(kwargs)
