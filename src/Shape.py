## @file Shape.py
#  @author  Joshua Sam Varughese, vaugj1
#  @brief  An interface for implementing masses, center of masses and inertia
#  @date  02/16/2021

from abc import ABC, abstractmethod

## @brief Shape provide an interface for different shapes
## @details The methods in the interface are abstract and need to be
# overridden by the modules that inherits this interface.


class Shape(ABC):

    @abstractmethod
    ## @brief a method to get the x cordinate of the center of mass of the shape
    # @return x cordinate of the center of mass
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief a method to get the y cordinate of the center of mass of the shape
    # @return the y cordinate of the center of mass
    def cm_y(self):
        pass

    @abstractmethod
    ## @brief a method to get the mass of the shape
    # @return the mass of the shape
    def mass(self):
        pass

    @abstractmethod
    ## @brief a method to get the interia of the shape
    # @return the value of inertia of the shape
    def m_inert(self):
        pass
