import argparse
import tkinter as tk
import cv2 as cv
from Func import FrameGetter


class App(tk.Tk):
    def __init__(self):
        super().__init__()


def run():
    app = App()
    app.mainloop()


def main(parser):
    parser.add_argument('-d', '--device')
    arg = parser.parse_args()

    device = arg.device
    getter = FrameGetter.CapObj(device)
    while True:
        cv.imshow('window', getter.frame)
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    del getter
    cv.destroyAllWindows()


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    main(args)
