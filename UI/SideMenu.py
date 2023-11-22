import tkinter as tk
from Func import Data


class Menu:
    __menu = None

    def __init__(self, root):
        self.data = Data.SideMenu()

        frame = tk.Frame(
            root,
            width=self.data.width,
            height=self.data.height,
            relief=self.data.relief,
            bg=self.data.bg
        )
        frame.place(x=self.data.x, y=self.data.y)

        self.menu = frame

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        self.__menu = value
