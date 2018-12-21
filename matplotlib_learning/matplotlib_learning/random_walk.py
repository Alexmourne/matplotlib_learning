from random import choice

class RandomWalk():
    """description of class"""

    def __init__(self, num_points=5000):
        """"""
        self.num_points = num_points

        #
        self.x_values = [0]
        self.y_values = [0]


    def get_step(self, direction=[1, -1], distance=[0, 1, 2, 3, 4]):
        """"""

        #
        self.direction = choice(direction)
        self.distance = choice(distance)
        step = self.direction * self.distance
        return step


    def fill_walk(self):
        """"""

        #
        while len(self.x_values) < self.num_points:
            #
            #x_direction = choice([1, -1])
            #x_distance = choice([0, 1, 2, 3, 4])
            #x_step = self.get_step([1, 0, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            x_step = self.get_step()

            #y_direction = choice([1, -1])
            #y_distance = choice([0, 1, 2, 3, 4])
            #y_step = self.get_step([1, 0, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            y_step = self.get_step()

            #
            if x_step == 0 and y_step == 0:
                continue

            #
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


