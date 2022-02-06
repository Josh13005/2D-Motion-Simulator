## @file TriangleT.py
#  @author Joshua Sam Varughese, varugj1
#  @brief Contains the TriangleT type to represent the mass, center of mass and inertia
#  @date 02/16/21

from Shape import Shape

## @brief TriangleT is used to represent the Triangle shape
#  @details inherits Shape


class TriangleT(Shape):

    ## @brief constructor for class TriangleT, represents the x-cordinate and
    #  y-coordinate of center of mass, the side and the mass of a triangle
    #  @param xs the x-coordinate of centre of mass
    #  @param ys the y-coordinate of centre of mass
    #  @param ss length of the side of the triangle
    #  @param ms the mass of the triangle
    #  @Exception throws value error if triangle side and mass are negative
    def __init__(self, xs, ys, ss, ms):
        if not (ss > 0 and ms > 0):
            raise ValueError
        self.x = xs
        self.y = ys
        self.s = ss
        self.m = ms

    ## @brief a method to get the x-cordinate of the center of mass of a triangle
    #  @return x-coordinate of the center of mass
    def cm_x(self):
        return self.x

    ## @brief a method to get the y-cordinate of the center of mass of a triangle
    #  @return y-coordinate of the center of mass
    def cm_y(self):
        return self.y

    ## @brief a method to get the mass of a triangle
    #  @return the mass of the triangle
    def mass(self):
        return self.m

    ## @brief a method to get the moment of interia of a triangle
    # @return the value of moment of inertia of the triangle
    def m_inert(self):
        return (self.m * self.s ** 2) / 12
