import matplotlib.pyplot as plt


def scatter_squares(x_values, y_values, s):
    
    if x_values == 0 and y_values == 0:
        #x_values = [1, 2, 3, 4, 5]
        #y_values = [1, 4, 9, 16, 25]
        x_values = list(range(1, 1001))
        y_values = [x**2 for x in x_values]
    
    #plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
    
    #'c' argument looks like a single numeric RGB or RGBA sequence,
    # which should be avoided as value-mapping will have precedence in
    # case its length matches with 'x' & 'y'.  Please use a 2-D array
    # with a single row if you really want to specify the same RGB or
    # RGBA value for all points.
    #plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
    
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
        edgecolor='none', s=s)
    
    #
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    
    #
    plt.tick_params(axis='both', which='major', labelsize=14)
    
    #
    plt.axis([0, 1100, 0, 1100000])
    
    plt.savefig('images\squares_plot.png', bbox_inches='tight')
    plt.show()

