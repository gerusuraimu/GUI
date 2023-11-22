class MainData:
    __title = 'window'
    __geometry = '1920x1080'

    @property
    def title(self):
        return self.__title

    @property
    def geometry(self):
        return self.__geometry


class TopMenu:
    __x = 0
    __y = 0
    __width = 1920
    __height = 75

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class SideMenu:
    __x = 0
    __y = 75
    __width = 150
    __height = 1080

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
