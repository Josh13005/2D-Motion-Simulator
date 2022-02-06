## @file Scene.py
#  @author John Popovici, popovj3
#  @brief Contains the Scene to run simulation on a shape
#  @date 2021-02-12

# from Shape import Shape
# unused import statement since working in terms of references to objects
from scipy.integrate import odeint

## @brief Scene is a class that runs a simulation for a shape
#  starting with initial velocities and unbalanced forces


class Scene:

    ## @brief constructor method for Scene
    #  @param s_prime a shape object
    #  @param F_x_prime an unbalanced force function in x dir
    #  @param F_y_prime an unbalanced force function in y dir
    #  @param v_x_prime a real number representing initial velocity in x dir
    #  @param v_y_prime a real number representing initial velocity in y dir
    def __init__(self, s_prime, F_x_prime, F_y_prime, v_x_prime, v_y_prime):
        self.s = s_prime
        self.F_x = F_x_prime
        self.F_y = F_y_prime
        self.v_x = v_x_prime
        self.v_y = v_y_prime

    ## @brief get the shape object
    #  @return a shape object
    def get_shape(self):
        return self.s

    ## @brief get the unbalanced force functions
    #  @return the unbalanced force functions
    def get_unbal_forces(self):
        return self.F_x, self.F_y

    ## @brief get the initial velocities
    #  @return the initial velocities
    def get_init_velo(self):
        return self.v_x, self.v_y

    ## @brief set the shape object
    #  @param s_prime a shape object
    def set_shape(self, s_prime):
        self.s = s_prime

    ## @brief set the unbalanced force functions
    #  @param F_x_prime an unbalanced force function in x dir
    #  @param F_y_prime an unbalanced force function in y dir
    def set_unbal_forces(self, F_x_prime, F_y_prime):
        self.F_x = F_x_prime
        self.F_y = F_y_prime

    ## @brief set the initial velocities
    #  @param v_x_prime a real number representing initial velocity in x dir
    #  @param v_y_prime a real number representing initial velocity in y dir
    def set_init_velo(self, v_x_prime, v_y_prime):
        self.v_x = v_x_prime
        self.v_y = v_y_prime

    ## @brief run the simulation on the shape object
    #  @param t_final a real number representing the final time
    #  @param nsteps an integer representing the number of steps
    #  @return lists representing values after simulation executed
    def sim(self, t_final, nsteps):
        t = []
        for i in range(nsteps):
            t.append(i * t_final / (nsteps - 1))
        return t, odeint(self.__ode__, [self.s.cm_x(), self.s.cm_y(),
                                        self.v_x, self.v_y], t)

    def __ode__(self, w, t):
        return [w[2], w[3], self.F_x(t) / self.s.mass(),
                self.F_y(t) / self.s.mass()]
