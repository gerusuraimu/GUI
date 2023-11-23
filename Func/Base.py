class FrameBase:
    def __init__(self, x, y, pad_x, pad_y, width, height, bg):
        self._x = x
        self._y = y
        self._pad_x = pad_x
        self._pad_y = pad_y
        self._width = width
        self._height = height
        self._bg = bg

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def pad_x(self):
        return self._pad_x

    @pad_x.setter
    def pad_x(self, value):
        self._pad_x = value

    @property
    def pad_y(self):
        return self._pad_y

    @pad_y.setter
    def pad_y(self, value):
        self._pad_y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def bg(self):
        return self._bg

    @bg.setter
    def bg(self, value):
        self._bg = value
