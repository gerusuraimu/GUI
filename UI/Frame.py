import tkinter as tk


class Frame:
    __frame = None

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

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, value):
        self.__frame = value
