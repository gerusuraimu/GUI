class MainData:
    __title = 'window'
    __geometry = '1920x1080'

    @property
    def title(self):
        return self.__title

    @property
    def geometry(self):
        return self.__geometry


class TopFrame:
    __x = 0
    __y = 0
    __pad_x = 5
    __pad_y = 5
    __width = 1920
    __height = 50
    __bg = 'white'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def pad_x(self):
        return self.__pad_x

    @property
    def pad_y(self):
        return self.__pad_y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def bg(self):
        return self.__bg


class SideFrame:
    __x = 0
    __y = 50
    __pad_x = 5
    __pad_y = 5
    __width = 150
    __height = 1080
    __bg = 'white'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def pad_x(self):
        return self.__pad_x

    @property
    def pad_y(self):
        return self.__pad_y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def bg(self):
        return self.__bg


class CanvasFrame:
    __x = 150
    __y = 50
    __pad_x = 5
    __pad_y = 5
    __width = 1920 - 150
    __height = 1080 - 50
    __bg = 'black'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def pad_x(self):
        return self.__pad_x

    @property
    def pad_y(self):
        return self.__pad_y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def bg(self):
        return self.__bg


class SideButton:
    __text0 = 'Rectangle'
    __text1 = 'Polygon'

    @property
    def text0(self):
        return self.__text0

    @property
    def text1(self):
        return self.__text1
