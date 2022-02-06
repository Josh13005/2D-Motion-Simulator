## @file Plot.py
#  @author Joshua Sam Varughese
#  @brief plots a graph of the simulation
#  @date 02/16/21

import matplotlib.pyplot as matplot

## @Brief plot grpahs for the simulation
#  @param w sequence of R
#  @param t is the argument passed to Fx and fy.


def plot(w, t):

    if not (len(w) == len(t)):
        raise ValueError

    else:
        x = []
        y = []

        for i in range(len(w)):
            x.append(w[i][0])

        for i in range(len(w)):
            y.append(w[i][1])

        fig, (graph1, graph2, graph3) = matplot.subplots(3)
        fig.suptitle("Motion Simulation")
        graph1.plot(t, x)
        graph2.plot(t, y)
        graph3.plot(x, y)

        graph1.set(ylabel="x (m)")
        graph2.set(ylabel="y (m)")
        graph3.set(ylabel="y (m)")
        graph3.set(xlabel="x (m)")
        matplot.show()
