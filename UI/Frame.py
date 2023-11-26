import tkinter as tk


class Frame:
    __frame = None
    __width = None
    __height = None

    def __init__(self, root, obj):
        frame = tk.Frame(
            root,
            width=obj.width,
            height=obj.height,
            padx=obj.pad_x,
            pady=obj.pad_y,
            bg=obj.bg
        )
        frame.place(x=obj.x, y=obj.y)

        self.frame = frame
        self.width = obj.width
        self.height = obj.height

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, value):
        self.__frame = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
