import tkinter as tk
from UI import Menu
from Func import Data


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)

        self.data = Data.MainData()
        self.m_dt = Data.TopMenu()
        self.s_dt = Data.SideMenu()
        self.c_dt = Data.Canvas()

        self.title(self.data.title)
        self.geometry(self.data.geometry)

        self.top_menu = Menu.Menu(
            self, self.m_dt.w, self.m_dt.h, self.m_dt.p_x, self.m_dt.p_y, self.m_dt.x, self.m_dt.y, self.m_dt.bg
        )
        self.side_menu = Menu.Menu(
            self, self.s_dt.w, self.s_dt.h, self.s_dt.p_x, self.s_dt.p_y, self.s_dt.x, self.s_dt.y, self.s_dt.bg
        )
        self.canvas_frame = Menu.Menu(
            self, self.c_dt.w, self.c_dt.h, self.c_dt.p_x, self.c_dt.p_y, self.c_dt.x, self.c_dt.y, self.c_dt.bg
        )


if __name__ == '__main__':
    app = App()
    app.mainloop()
