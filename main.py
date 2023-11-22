import tkinter as tk
import cv2 as cv
from UI import SideMenu
from Func import Data, FrameGetter


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.m_data = Data.MainData()
        self.s_data = Data.SideMenu()

        self.top_menu = SideMenu.Menu(self, self.m_data.width, self.m_data.height, self.m_data.x, self.m_data.y)
        self.side_menu = SideMenu.Menu(self, self.s_data.width, self.s_data.height, self.s_data.x, self.s_data.y)

        self.ui_init()

    def ui_init(self):
        self.title(self.m_data.title)
        self.geometry(self.m_data.geometry)


if __name__ == '__main__':
    app = App()
    app.mainloop()
