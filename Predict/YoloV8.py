from ultralytics import YOLO


class Predict:
    __name = None
    __model = None

    def __init__(self, name):
        self.name = name
        self.model = self.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = YOLO(value)

    def predict(self, frame):
        results = self.model.predict(frame)
        return results
