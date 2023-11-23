from Predict import Base


class Predict(Base.YoloBase):
    def __init__(self, name):
        super().__init__(name)

    def predict(self, frame):
        results = self.model.predict(frame)
        return results
