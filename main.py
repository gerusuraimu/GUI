import cv2 as cv
import tkinter as tk
from UI import Frame, Button
from Func import Data, FrameGetter
from PIL import Image, ImageTk, ImageOps


class App(tk.Tk):
    __fps = 1000 // 60
    __photo_image = None

    def __init__(self):
        super().__init__()
        self.frame_getter = FrameGetter.CapObj('./result.mp4')
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

        self.canvas = tk.Canvas(self.canvas_frame.frame, width=self.canvas_frame.width, height=self.canvas_frame.height)
        self.canvas.pack(expand=True)

        self.side_button = Button.SideMenu(self.side_menu.frame)

        self.disp_id = None
        self.canvas.bind('<Button-1>', self.__canvas_click)

    def __canvas_click(self, event):
        if self.disp_id is None:
            self.disp_image()
        else:
            self.after_cancel(self.disp_id)
            self.disp_id = None

    def disp_image(self):
        frame = self.frame_getter.frame
        if frame is None:
            return

        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image = Image.fromarray(image)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        image = ImageOps.pad(image, (canvas_width, canvas_height))
        self.photo_image = ImageTk.PhotoImage(image=image)

        self.canvas.delete('all')
        self.canvas.create_image(
            canvas_width / 2,
            canvas_height / 2,
            image=self.photo_image
        )

        self.disp_id = self.after(self.fps, self.disp_image)

    @property
    def fps(self):
        return self.__fps

    @fps.setter
    def fps(self, value):
        self.__fps = 1000 // value

    @property
    def photo_image(self):
        return self.__photo_image

    @photo_image.setter
    def photo_image(self, value):
        self.__photo_image = value


if __name__ == '__main__':
    app = App()
    app.mainloop()
