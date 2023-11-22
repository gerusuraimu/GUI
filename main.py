import tkinter as tk
import cv2 as cv
from Func import Data, FrameGetter


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.data = Data.Data()
        self.ui_init()

    def ui_init(self):
        self.title(self.data.title)
        self.geometry(self.data.geometry)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
