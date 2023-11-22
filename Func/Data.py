import tkinter as tk


class MainData:
    __title = 'window'
    __geometry = '1920x1080'
    __x = 0
    __y = 0
    __width = 1920
    __height = 75

    @property
    def title(self):
        return self.__title

    @property
    def geometry(self):
        return self.__geometry

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class SideMenu:
    __x = 0
    __y = 75
    __bg = 'white'
    __width = 150
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