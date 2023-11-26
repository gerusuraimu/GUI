import tkinter as tk
from Func import Data


class SideMenu:
    __button0 = None
    __button1 = None
    __button2 = None

    def __init__(self, obj):
        self.__data = Data.SideButton()
        self.__obj = obj

        self.__button()
        self.__place()

    def __button(self):
        self.__button0 = tk.Button(self.__obj, text=self.__data.text0, width=20, height=1)
        self.__button1 = tk.Button(self.__obj, text=self.__data.text1, width=20, height=1)
        self.__button2 = tk.Button(self.__obj, text=self.__data.text2, width=20, height=1)

    def __place(self):
        self.button0.place(x=0, y=0)
        self.button1.place(x=0, y=25)
        self.button2.place(x=0, y=50)

    @property
    def button0(self):
        return self.__button0

    @property
    def button1(self):
        return self.__button1

    @property
    def button2(self):
        return self.__button2
