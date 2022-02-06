## @file Body.py
#  @author John Popovici, popovj3
#  @brief Contains the BodyT type to represent a body shape
#  @date 2021-02-12

from Shape import Shape

## @brief BodyT is a class that implements an ADT for
#  a body that is of a shape


class BodyT(Shape):

    ## @brief constructor method for BodyT
    #  @param x_s a list of real numbers representing center of mass on x axis
    #  @param y_s a list of real numbers representing center of mass on y axis
    #  @param m_s a list of real numbers representing mass
    #  @throws Exception ValueError if parameter list lengths are not equal
    #  or any members of m_s are not greater than 0 or the calculated moment
    #  is less than 0
    def __init__(self, x_s, y_s, m_s):
        if len(x_s) != len(y_s) or len(y_s) != len(m_s):
            raise ValueError
        for mu in m_s:
            if mu <= 0:
                raise ValueError
        self.cmx = self.__cm__(x_s, m_s)
        self.cmy = self.__cm__(y_s, m_s)
        self.m = self.__sum__(m_s)
        self.moment = self.__mmom__(x_s, y_s, m_s) - self.__sum__(m_s) * \
            (self.__cm__(x_s, m_s) ** 2 + self.__cm__(y_s, m_s) ** 2)
        if self.moment < 0:
            raise ValueError

    ## @brief get the center of mass on x axis
    #  @return a real number representing the center of mass on x axis
    def cm_x(self):
        return self.cmx

    ## @brief get the center of mass on y axis
    #  @return a real number representing the center of mass on y axis
    def cm_y(self):
        return self.cmy

    ## @brief get the mass
    #  @return a real number representing the mass
    def mass(self):
        return self.m

    ## @brief get the moment of inertia
    #  @return a real number representing the moment of inertia
    def m_inert(self):
        return self.moment

    @staticmethod
    def __sum__(m_s):
        out = 0
        for mu in m_s:
            out += mu
        return out

    @staticmethod
    def __cm__(z, m):
        top = 0
        bot = 0
        for i in range(len(m)):
            top += z[i] * m[i]
            bot += m[i]
        return top / bot

    @staticmethod
    def __mmom__(x, y, m):
        out = 0
        for i in range(len(m)):
            out += m[i] * (x[i] ** 2 + y[i] ** 2)
        return out
