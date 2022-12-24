""""This module contains the class to plot the vectors of the mecanum wheels."""

import matplotlib.pyplot as plt
import random
from math import sin, cos, pi, tan, atan, sqrt, radians, degrees

# Define the class to plot the vectors:
class PlotVector:

    # Attribute to store all of the vectors:
    vectors = list()
    # Attribute to store the direction of the net vector:
    direction = int()

    # Define the constructor for graphing two vectors:
    def __init__ (self, title, vectors):
        """Create a class to plot the vectors and the result vector:
        """
        self.title = title
        # Creates a nested list to store the vectors:
        self.vectors = vectors
        return None
    
    # Create a instance of the class for plotting the mecanum vectors:
    @classmethod
    def mecanum_vectors(cls, title, direction):
        """Create a class to plot the vectors and the result vector:
        """
        return cls(title, direction)

    def magnitudes(self, direction):
        """Calculate the components of the vectors."""
        # Convert the direction to radians:
        direction = radians(direction)
        # Calculate the magnitude of the vectors:
        motor1 = 0 - sin(direction)
        motor2 = 0 + cos(direction)
        motor3 = motor1
        motor4 = motor2
        # Calculate the x and y components of the vectors:
        x_comp1 = cos(pi/4) * motor1
        y_comp1 = sin(pi/4) * motor1
        x_comp2 = cos(3 * pi/4) * motor2
        y_comp2 = sin(3 * pi/4) * motor2
        x_comp3 = cos(5 * pi/4) * motor3
        y_comp3 = sin(5 * pi/4) * motor3
        x_comp4 = cos(7 * pi/4) * motor4
        y_comp4 = sin(7 * pi/4) * motor4
    # [[x_vector_1, y_vector_1], [x_vector_2, y_vector_2], [x_vector_3, y_vector_3], [x_vector_4, y_vector_4]]
        self.vectors = [[x_comp1, y_comp1], [x_comp2, y_comp2], [x_comp3, y_comp3], [x_comp4, y_comp4]]
        return None

    # Plot the vectors:
    def plot(self):
        """Plot the vectors the vectors and the result vector."""
        # Calculate the result vector:
        self.result_vector = [sum([vector[0] for vector in self.vectors]), sum([vector[1] for vector in self.vectors])]
        # Create the plot:
        plt.xlabel('x')
        plt.ylabel('y')
        # Biggest vector:
        biggest_vector = max([sqrt(vector[0]**2 + vector[1]**2) for vector in self.vectors])
        # Fix the x and y limits:
        plt.xlim(-biggest_vector, biggest_vector)
        plt.ylim(-biggest_vector, biggest_vector)
        # Plot the x and y axis:
        plt.axhline(y = 0, color = 'black')
        plt.axvline(x = 0, color = 'black')
        # Plot the vectors:
        plt.arrow(x = 0, y = 0, dx = self.vectors[0][0], dy = self.vectors[0][1], head_width = 0.1, head_length = 0.1, facecolor = random.choice(['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black']))
        plt.arrow(x = 0, y = 0, dx = self.vectors[1][0], dy = self.vectors[1][1], head_width = 0.1, head_length = 0.1, facecolor = random.choice(['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black']))
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
    # Test the class method:
    plot = PlotVector.mecanum_vectors('Mecanum Vectors', 90)
    # Test the magnitudes method:
    plot.magnitudes(45)
    # Test the plot method:
    plot.plot()