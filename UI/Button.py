import tkinter as tk
from Func import Data


class SideMenu:
    __button0 = None
    __button1 = None

    def __init__(self, obj):
        self.__data = Data.SideButton()
        self.__obj = obj

        self.__button()

    def __button(self):
        self.button0 = tk.Button(self.__obj, text=self.__data.text0)
        self.button1 = tk.Button(self.__obj, text=self.__data.text1)

    @property
    def button0(self):
        return self.__button0

    @button0.setter
    def button0(self, value):
        self.__button0 = value

    @property
    def button1(self):
        return self.__button1

    @button1.setter
    def button1(self, value):
        self.__button1 = value
