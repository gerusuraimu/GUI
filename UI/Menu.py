import tkinter as tk


class Menu:
    __menu = None

    def __init__(self, root, width, height, pad_x, pad_y, x, y, bg):
        frame = tk.Frame(root, width=width, height=height, padx=pad_x, pady=pad_y, bg=bg)
        frame.place(x=x, y=y)

        self.menu = frame

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value
