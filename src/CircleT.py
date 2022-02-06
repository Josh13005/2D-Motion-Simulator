## @file CircleT.py
#  @author Joshua Sam Varughese, varugj1
#  @brief Contains the CircleT type to represent the mass, center of mass and inertia
#  @date 02/16/21

from Shape import Shape

## @brief CircleT is used to represent the circle shape
#  @details inherits Shape


class CircleT(Shape):

    ## @brief constructor for class CircleT, represents the x-cordinate and
    #  y-coordinate of center of mass, radius and the mass of a circle
    #  @param xs the x-coordinate of centre of mass
    #  @param ys the y-coordinate of centre of mass
    #  @param rs the radius of the circular body
    #  @param ms the mass of the circle
    #  @Exception throws value error if radius and mass are negative
    def __init__(self, xs, ys, rs, ms):
        if not(rs > 0 and ms > 0):
            raise ValueError
        self.x = xs
        self.y = ys
        self.r = rs
        self.m = ms

    ## @brief a method to get the x-cordinate of the center of mass of a circle
    #  @return x-coordinate of the center of mass
    def cm_x(self):
        return self.x

    ## @brief a method to get the y-cordinate of the center of mass of a circle
    #  @return y-coordinate of the center of mass
    def cm_y(self):
        return self.y

    ## @brief a method to get the mass of a circle
    #  @return the mass of the circle
    def mass(self):
        return self.m

    ## @brief a method to get the moment of interia of a circle
    # @return the value of moment of inertia of the circle
    def m_inert(self):
        return (self.m * self.r ** 2) / 2
