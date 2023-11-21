import cv2 as cv


class Obj:
    __cap = None
    __frame = None
    __device = None

    @property
    def cap(self):
        return self.__cap

    @cap.setter
    def cap(self, value):
        self.__cap = cv.VideoCapture(value)

    @property
    def frame(self):
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
