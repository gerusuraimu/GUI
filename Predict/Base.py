from ultralytics import YOLO


class YoloBase:
    _name = None
    _model = None

    def __init__(self, name):
        self.name = name
        self.model = self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = YOLO(value)