import tkinter as tk
from UI import Frame, Button
from Func import Data


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)

        self.data = Data.MainData()
        self.top_data = Data.TopFrame()
        self.side_data = Data.SideFrame()
        self.canvas_data = Data.CanvasFrame()

        self.title(self.data.title)
        self.geometry(self.data.geometry)

        self.top_menu = Frame.Frame(self, self.top_data)
        self.side_menu = Frame.Frame(self, self.side_data)
        self.canvas_frame = Frame.Frame(self, self.canvas_data)

        self.side_button = Button.SideMenu(self.side_menu.frame)


if __name__ == '__main__':
    app = App()
    app.mainloop()
