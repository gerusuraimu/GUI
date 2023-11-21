import threading
import cv2 as cv


class CapObj:
    __cap = None
    __frame = None
    __device = None

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
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                self.__frame = frame
            else:
                self.__frame = None
        return self.__frame

    @property
    def device(self):
        return self.__device

    @device.setter
    def device(self, value):
        self.__device = value
        self.cap = self.device

    def save(self, name):
        task = threading.Thread(target=cv.imwrite, args=(name, self.frame))
        task.start()


class ImageObj:
    __files = None

