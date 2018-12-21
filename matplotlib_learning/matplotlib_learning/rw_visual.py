import matplotlib.pyplot as plt

from random_walk import RandomWalk
import scatter_squares as ss

#
while True:
    #
    #rw = RandomWalk()
    rw = RandomWalk(50000)
    rw.fill_walk()

    #
    plt.figure(dpi=130.43, figsize=(14, 8))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolors='none', s=1)

    #
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
        s=100)

    #Adding an axes using the same arguments as a previous axes currently 
    # reuses the earlier instance.  In a future version, a new instance will 
    # always be created and returned.  Meanwhile, this warning can be 
    # suppressed, and the future behavior ensured, by passing a unique label 
    # to each axes instance.
    #"Adding an axes using the same arguments as a previous axes "
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    #ss.scatter_squares(rw.x_values, rw.y_values, s=15)

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

