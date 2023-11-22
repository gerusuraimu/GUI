import tkinter as tk


class MainData:
    __title = 'window'
    __geometry = '1920x1080'

    @property
    def title(self):
        return self.__title

    @property
    def geometry(self):
        return self.__geometry


class SideMenu:
    __x = 0
    __y = 0
    __bg = 'white'
    __width = 100
    __height = 1080
    __relief = tk.SOLID

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def bg(self):
        return self.__bg

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def relief(self):
        return self.__relief
