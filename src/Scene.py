## @file Scene.py
#  @author Joshua Sam Varughese, varugj1
#  @brief Contains the Scene type to represent type of shape, force, velocity of a shape
#  @date 02/16/21
#  @details Scene is used to set and get force, velocity and type of shape

from scipy.integrate import odeint


class Scene:

    ## @brief constructor for class Scene, represents the x-cordinate and
    #  y-coordinate of force and velocity and the type of shape
    #  @param sp the type of the shape
    #  @param Fpx the x-coordinate of the force
    #  @param Fpy the y-coordinate of the force
    #  @param vpx the x-coordinate of the velocity
    #  @param vpy the y-coordinate of the velocity
    def __init__(self, sp, Fpx, Fpy, vpx, vpy):

        self.s = sp
        self.Fx = Fpx
        self.Fy = Fpy
        self.vx = vpx
        self.vy = vpy

    ## @brief a method to get the type of shape
    #  @return the shape of the body
    def get_shape(self):
        return self.s

    ## @brief a method to get the unbalanced forces of the shape
    #  @return the unbalanced force at the x-coordinate and y-coordinate
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief a method to get the velocity of the shape
    #  @return the x-coordinate and y-coordinate of the velocity
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief a method to set the type of shape
    def set_shape(self, sp):
        self.s = sp

    ## @brief a method to set the forces
    def set_unbal_forces(self, Fpx, Fpy):
        self.Fx, self.Fy = Fpx, Fpy

    ## @brief a method to set the velocities
    def set_init_velo(self, vpx, vpy):
        self.vx, self.vy = vpx, vpy

    ## @brief a method to simulate the motion of a body
    #  @param t_final is the final time.
    #  @param the number of steps or positions.
    #  @return the time and the position and the velocity of the body under the forces
    #  specified.
    def sim(self, t_final, nsteps):
        t = [i * t_final / (nsteps - 1) for i in range(0, nsteps - 1)]
        return t, odeint(self.ode, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)

    ## @brief a local function that gives the sequnce n elements with type R
    #  @param w a sequence of R
    #  @param t an argument paired to Fx and Fy
    def ode(self, w, t):
        return [w[2], w[3], (self.Fx(t)) / (self.s.mass()), (self.Fy(t)) / (self.s.mass())]
