# Create a class to plot the vectors and the result vector:
#     class PlotVectors:

import matlibplot.pyplot as plt
import random
import math

# Define the class to plot the vectors:
class PlotVector:

    # Attribute to store all of the vectors:
    vectors = list()

    # Define the constructor for graphing two vectors:
    def __init__ (self, title, vector_1, vector_2):
        """Create a class to plot the vectors and the result vector:
        """
        self.title = title
        # Creates a nested list to store the vectors:
        self.vectors = [vector_1, vector_2]


        pass
    
    # Create a instance of the class for plotting the mecanum vectors:
    @classmethod
    def mecanum_vectors(cls, label, direction):
        """Create a class to plot the vectors and the result vector:
        """
        cls.vector_1 = 45
        cls.vector_2 = 135
        cls.vector_3 = 225
        cls.vector_4 = 315
        return cls(label, direction)

    def magnitudes(self, direction):
        motor1 = 0 - math.sin(direction )
        motor2 = math.cos(direction)
        motor3 = motor1
        motor4 = motor2

    # Plot the vectors:
    def plot(self):
        """Plot the vectors the vectors and the result vector."""
        # Create the plot:
        plt.xlabel('x')
        plt.ylabel('y')
        # Plot the x and y axis:
        plt.axhline(y = 0, color = 'black')
        plt.axvline(x = 0, color = 'black')
        # Plot the vectors:
        for vector in self.vectors:
            plt.arrow(x = 0, y = 0, dx = vector[0], dy = vector[1], head_width = 0.1, head_length = 0.1, facecolor = random.choice(['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black']))
        # Plot the result vector:
        plt.arrow(x = 0, y = 0, dx = self.result_vector[0], dy = self.result_vector[1], head_width = 0.1, head_length = 0.1, facecolor = 'black')
        # Add a grid:
        plt.grid(linestyle = '--')
        # Add a title:
        plt.title(self.title)
        # Add a legend describing the vectors:
        plt.legend(['Vector 1', 'Vector 2', 'Result'], loc = 'upper right')
        # Show the plot:
        plt.show()

        
# test the class:
if __name__ == '__main__':
    # Create a instance of the class:
    vector_plot = PlotVector('Mecanum Vectors', [1, 2], [3, 4])
    # Plot the vectors:
    vector_plot.plot()
