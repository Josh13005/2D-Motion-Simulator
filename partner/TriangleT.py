## @file TriangleT.py
#  @author John Popovici, popovj3
#  @brief Contains the TriangleT type to represent a triangle shape
#  @date 2021-02-12

from Shape import Shape

## @brief TriangleT is a class that implements an ADT for the
#  mathematical concept of an equilateral triangle


class TriangleT(Shape):

    ## @brief constructor method for TriangleT
    #  @param x_s a real number representing the center of mass on x axis
    #  @param y_s a real number representing the center of mass on y axis
    #  @param s_s a real number representing the side lengths
    #  @param m_s a real number representing the mass
    #  @throws Exception ValueError if s_s or m_s not greater than 0
    def __init__(self, x_s, y_s, s_s, m_s):
        if s_s <= 0 or m_s <= 0:
            raise ValueError
        self.x = x_s
        self.y = y_s
        self.s = s_s
        self.m = m_s

    ## @brief get the center of mass on x axis
    #  @return a real number representing the center of mass on x axis
    def cm_x(self):
        return self.x

    ## @brief get the center of mass on y axis
    #  @return a real number representing the center of mass on y axis
    def cm_y(self):
        return self.y

    ## @brief get the mass
    #  @return a real number representing the mass
    def mass(self):
        return self.m

    ## @brief get the moment of inertia
    #  @return a real number representing the moment of inertia
    def m_inert(self):
        return self.m * (self.s ** 2) / 12.0
