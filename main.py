# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi('Hello World!')
    print('Goodbye World!')
    print_hi('Welcome GitHub!')

screen_width = 800
screen_height = 600

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Who committed this entry yet

mobile_width = 300
mobile_height = 400


# this is local branch1 comment line2
# here comes another line of comment
# yet another brilliant idea

class Animal:
    def __init__(self, species: str, kingdom: str):
        """

        :type kingdom: object
        """
        self.kingdom = kingdom
        self.species = species

    def __str__(self, name ):
        return f'Animal name {name}, of {self.species} form {self.kingdom}'


class Dog(Animal):
    def __init__(self, species, kingdom, race: str):
        super().__init__(species, kingdom)
        self.race = race
