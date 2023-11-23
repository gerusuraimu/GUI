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
    __p_x = 5
    __p_y = 5
    __w = 1920
    __h = 50
    __bg = 'white'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def p_x(self):
        return self.__p_x

    @property
    def p_y(self):
        return self.__p_y

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def bg(self):
        return self.__bg


class SideMenu:
    __x = 0
    __y = 50
    __p_x = 5
    __p_y = 5
    __w = 150
    __h = 1080
    __bg = 'white'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def p_x(self):
        return self.__p_x

    @property
    def p_y(self):
        return self.__p_y

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def bg(self):
        return self.__bg


class Canvas:
    __x = 150
    __y = 50
    __p_x = 5
    __p_y = 5
    __w = 1920 - 150
    __h = 1080 - 50
    __bg = 'black'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def p_x(self):
        return self.__p_x

    @property
    def p_y(self):
        return self.__p_y

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def bg(self):
        return self.__bg
