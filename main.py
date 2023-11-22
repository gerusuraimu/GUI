import tkinter as tk
import cv2 as cv
from UI import SideMenu
from Func import Data, FrameGetter


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.main_data = Data.MainData()
        self.side_data = Data.SideMenu()
        self.side_menu = SideMenu.Menu(self)

        self.ui_init()

    def ui_init(self):
        self.title(self.main_data.title)
        self.geometry(self.main_data.geometry)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
