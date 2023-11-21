import tkinter as tk
from Func import FrameGetter


class App(tk.Tk):
    def __init__(self):
        super().__init__()


def run():
    app = App()
    app.mainloop()


def main():
    getter = FrameGetter.CapObj()
    print(getter)


if __name__ == '__main__':
    main()
