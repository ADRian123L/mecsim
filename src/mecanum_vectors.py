""""This module contains the class to plot the vectors of the mecanum wheels."""

import matplotlib.pyplot as plt
import random
import base64
import io
from math import sin, cos, pi, sqrt, radians
import string

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
        # Change the attribute to store the direction of the net vector:
        cls.direction = direction
        return cls(title, direction)

    def magnitudes(self):
        """Calculate the components of the vectors."""
        # Constants:
        COSTANT_45 = 1/sqrt(2)
        GROWER = 2
        NEGATIVE = -1
        # Convert the direction to radians:
        direction = radians(self.direction) + pi/4
        # Calculate the magnitude of the vectors:
        motor1 = 0 - cos(direction)# The motor's vector points at a 135 degree angle.
        motor2 = 0 + sin(direction) # The motor's vector points at a 45 degree angle.
        motor3 = motor1 # The motor's vector points at a 135 degree angle.
        motor4 = motor2 # The motor's vector points at a 45 degree angle.
        # Calculate the x and y components of the vectors:
        x_comp1 = COSTANT_45 * motor1 * GROWER * NEGATIVE# The motor's vector points at a 135 degree angle.
        y_comp1 = COSTANT_45 * motor1 * GROWER# The motor's vector points at a 135 degree angle.
        x_comp2 = COSTANT_45 * motor2 * GROWER# The motor's vector points at a 45 degree angle.
        y_comp2 = COSTANT_45 * motor2 * GROWER# The motor's vector points at a 45 degree angle.
        x_comp3 = COSTANT_45 * motor3 * NEGATIVE# The motor's vector points at a 135 degree angle. 
        y_comp3 = COSTANT_45 * motor3 # The motor's vector points at a 135 degree angle.
        x_comp4 = COSTANT_45 * motor4 # The motor's vector points at a 45 degree angle.
        y_comp4 = COSTANT_45 * motor4 # The motor's vector points at a 45 degree angle.
    # [[x_vector_1, y_vector_1], [x_vector_2, y_vector_2], [x_vector_3, y_vector_3], [x_vector_4, y_vector_4]]
        self.vectors = [[x_comp1, y_comp1], [x_comp2, y_comp2], [x_comp3, y_comp3], [x_comp4, y_comp4]]
        # Print the vectors:
        print(self.vectors)
        return None

    # Create a method for saving the plot as an image:
    def save_plot(self, filename):
        """Save the plot as an image."""
        # Save the plot:
        plt.savefig(filename, format='png', dpi=100)
        # Close the plot:
        if hasattr(plt, 'close'):
            plt.close()
        return None

    # A function that converts a plt to a image data string:
    def plt_to_img_str(plt, width=500, dpi=100):
        """Converts matplotlib plt to image data string."""
        try:
            # Create a buffer to store the image:
            imgdata = io.BytesIO()
            # Save the image to the buffer:
            plt.savefig(imgdata, format='png', dpi=dpi)
            # Close the plot:
            if hasattr(plt, 'close'):
                plt.close()
            # Reset the buffer to the start:
            imgdata.seek(0)
            # Create a string to store the image:
            img_str = "data:image/png;base64," +  base64.b64encode(imgdata.getvalue()).decode("utf-8")
            # Return the image string:
            return "<img src='" + img_str + "' width='" + str(width) + "'>"  # Return the image data string
        except Exception as error:
            return f"Error: Failed to render the plot: {error}"  # Return the error message

    # Plot the vectors:
    def plot(self, mecanum=False, png_image=False):
        """Plot the vectors the vectors and the result vector."""
        # Calculate the result vector:
        if mecanum:
            self.result_vector = [cos(radians(self.direction)), sin(radians(self.direction))]
        else:
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
        for vector in self.vectors[:]:
            plt.arrow(x = 0, y = 0, dx = vector[0], dy = vector[1], head_width = 0.1, head_length = 0.1, facecolor = random.choice(['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black']))
        # Plot the result vector:
        plt.arrow(x = 0, y = 0, dx = self.result_vector[0], dy = self.result_vector[1], head_width = 0.1, head_length = 0.1, facecolor = 'black')
        print(self.result_vector)
        # Add a grid:
        plt.grid(linestyle = '--')
        # Add a title:
        plt.title(self.title)
        # Creates a list to store the labels all of the vectors and the result vector:
        labels = list()
        # Add the labels for the vectors:
        for i in range(len(self.vectors)):
            labels.append(f'Vector {i + 1}')
        # Add the label for the result vector:
        labels.append('Result')
        # Add the legend:
        plt.legend(labels, loc = 'upper right')
        # Different forms to return the plot:
        if png_image:
            # Create a different name for the image:
            filename = 'plot.png' + random.randint(0, 500)
            # Save the plot:
            self.save_plot(filename=filename)
            # Return the plot:
            return None
        # Save the plot as a string:
        image = self.plt_to_img_str(plt)
        # Return the image:
        return image

# A main function that takes a direction and plots the vectors:
def main( inputs ):
    """ The function drives the program."""
    # Assign the inputs to variables:
    try:
        x_1 = inputs["x_1"]
        y_1 = inputs["y_1"]
        x_2 = inputs["x_2"]
        y_2 = inputs["y_2"]
    except:
        assert "Error: Invalid input"
    # Create a list to store the vectors:
    vectors = list()
    # Add the vectors to the list:
    vectors.append([x_1, y_1])
    vectors.append([x_2, y_2])
    # Plot the vectors using the class:
    plot = PlotVector('Vector Addition', vectors)
    image = plot.plot()
    # Create an instance of the class method:
    plot_mecanum = PlotVector('Mecanum Wheel', inputs["angle"])
    plot_mecanum.magnitudes()
    image_mecanum = plot_mecanum.plot(mecanum=True)
    # Return the images in a dictionary:
    return {"image": image, "image_mecanum": image_mecanum, "x_1": x_1, "y_1": y_1, "x_2":  x_2, "y_2": y_2}

# test the class:
if __name__ == '__main__':
    # Create an object to plot a mecannum wheel:
    plot_mecanum = PlotVector('Mecanum Wheel', 45)
    plot_mecanum.magnitudes()
    image_mecanum = plot_mecanum.plot(mecanum=True, png_image=True)
    # Create an object to plot a vector addition:
    plot = PlotVector('Vector Addition', [[1, 2], [3, 4]])
    image = plot.plot(png_image=True)