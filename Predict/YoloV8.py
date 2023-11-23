from Predict import Base
from ultralytics import YOLO


class Predict(Base.YoloBase):
    def __init__(self, name='yolov8n.pt'):
        super().__init__(name)

    def predict(self, frame):
        results = self.model.predict(frame)
        return results
