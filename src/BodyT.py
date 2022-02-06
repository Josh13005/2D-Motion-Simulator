## @file BodyT.py
#  @author Joshua Sam Varughese, varugj1
#  @brief Contains the BodyT type to represent the mass, center of mass and inertia
#  @date 02/16/2021

from Shape import Shape

## @brief BodyT is used to represent an abstract shape
# detials Inherits from Shape


class BodyT(Shape):

    ## @brief constructor for class BodyT, represents the x-cordinate and
    #  y-coordinate of center of mass and the mass of a body
    #  @param xs the x-coordinate of centre of mass
    #  @param ys the y-coordinate of centre of mass
    #  @param ms the mass of the triangle
    #  @Exception throws value error if length of sequence of centre of masses and the mass
    #  are different and if the sequence of mass is contains negative number
    def __init__(self, xs, ys, ms):

        if not (len(xs) == len(ys) == len(ms)) and \
                (not ([ms[i] > 0 for i in range(len(ms))])):
            raise ValueError()

        self.cmx = cm(xs, ms)
        self.cmy = cm(ys, ms)
        self.m = sum(ms)
        self.moment = mmom(xs, ys, ms) - sum(ms) * (cm(xs, ms) ** 2 + cm(ys, ms) ** 2)

    ## @brief a method to get the x-cordinate of the center of mass of a body
    #  @return x-coordinate of the center of mass
    def cm_x(self):
        return self.cmx

    ## @brief a method to get the y-cordinate of the center of mass of a body
    #  @return y-coordinate of the center of mass
    def cm_y(self):
        return self.cmy

    ## @brief a method to get the mass of a body
    #  @return the mass of the body
    def mass(self):
        return self.m

    ## @brief a method to get the moment of interia of a body
    # @return the value of moment of inertia of the body
    def m_inert(self):
        return self.moment

## @brief a method to get the total centre of mass of a given sequence
#  @param z is the sequence of centre of mass
#  @param m is the sequence of masses
#  @return the total value of center of mass


def cm(z, m):
    tot = 0
    for i in range(0, len(m)):
        tot += z[i] * m[i]
    return tot / sum(m)

## @brief a method to get the total moment of inertia of a given sequence
#  @param x is the sequence of x-coordinate of centre of mass
#  @param y is the sequence of y-coordinate of centre of mass
#  @param m is the sequence of mass
#  @return the total value of moment of inertia


def mmom(x, y, m):
    tot = 0
    for i in range(0, len(m)):
        tot += m[i] * (x[i] ** 2 + y[i] ** 2)
    return tot
