import queue
import threading
import cv2 as cv


class CapObj:
    __cap = None
    __frame = None
    __device = None
    __frame_queue = queue.Queue()

    def __init__(self, device=None):
        if device is not None:
            self.device = device

    def __del__(self):
        if self.cap is not None:
            self.cap.release()

    def __repr__(self):
        cap = self.cap is not None
        device = self.device is not None
        return f'cap = {cap}\ndevice = {device}\nCapObj enable = {cap and device}'

    @property
    def cap(self):
        return self.__cap

    @cap.setter
    def cap(self, value):
        self.__cap = cv.VideoCapture(value)

    @property
    def frame(self):
        self.__frame = self.__frame_queue.get()
        self.__get_frame()
        return self.__frame

    @property
    def device(self):
        return self.__device

    @device.setter
    def device(self, value):
        self.__device = value
        self.cap = self.device
        self.__get_frame()

    def __get_frame(self):
        task = threading.Thread(target=self.__getter, args=(self.__frame_queue, self.cap))
        task.start()

    @staticmethod
    def __getter(q, cap):
        ret, frame = cap.read()
        if not ret:
            frame = None
        q.put(frame)

    def save(self, name):
        task = threading.Thread(target=cv.imwrite, args=(name, self.frame))
        task.start()


class ImageObj:
    __files = None
    __image = None
    __image_queue = queue.Queue()

