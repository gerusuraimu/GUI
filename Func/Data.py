from Func import Base


class MainData:
    __title = 'window'
    __geometry = '1920x1080'

    @property
    def title(self):
        return self.__title

    @property
    def geometry(self):
        return self.__geometry


class TopFrame(Base.FrameBase):
    def __init__(self):
        super().__init__(x=0, y=0, pad_x=5, pad_y=5, width=1920, height=50, bg='white')


class SideFrame(Base.FrameBase):
    def __init__(self):
        super().__init__(x=0, y=50, pad_x=0, pad_y=0, width=150, height=1080, bg='white')


class CanvasFrame(Base.FrameBase):
    def __init__(self):
        super().__init__(x=150, y=50, pad_x=0, pad_y=0, width=1770, height=1030, bg='black')


class SideButton:
    __text0 = 'Start'
    __text1 = 'Stop'
    __text2 = 'Exit'

    @property
    def text0(self):
        return self.__text0

    @property
    def text1(self):
        return self.__text1

    @property
    def text2(self):
        return self.__text2
