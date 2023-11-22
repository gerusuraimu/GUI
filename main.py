import tkinter as tk
import cv2 as cv
from Func import FrameGetter


class App(tk.Tk):
    def __init__(self):
        super().__init__()


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
