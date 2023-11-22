import tkinter as tk


class Menu:
    __menu = None

    def __init__(self, root, width, height, x, y):
        frame = tk.Frame(
            root,
            width=width,
            height=height,
            bg='white'
        )
        frame.place(x=x, y=y)

        self.menu = frame

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value
