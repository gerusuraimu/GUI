import tkinter as tk
from Func import Data


class Menu:
    __menu = None

    def __init__(self, root, width, height, x, y):
        self.data = Data.SideMenu()

        frame = tk.Frame(
            root,
            width=width,
            height=height,
            bg=self.data.bg
        )
        frame.place(x=x, y=y)

        self.menu = frame

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value
