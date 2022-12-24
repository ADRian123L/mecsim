import matplotlib.pyplot as plt
import numpy as np
import base64
import io
import os
from PIL import Image
import math


class Macanum:
    def __init__(self,x):
        self.const = math.cos(math.radians(45))
        self.radians = math.pi * x
        print(self.radians)
        self.radians = self.radians + 45 * (math.pi / 180)
        print(self.radians)
        self.motor1_vel = (0 - math.cos(self.radians)) * self.const
        print(self.motor1_vel)
        
        self.motor2_vel = math.sin(self.radians) * self.const
        
        
        self.motor3_vel = self.motor1_vel
        
        
        self.motor4_vel = self.motor2_vel
        
        
        self.result_x =2 * (-self.motor1_vel + self.motor2_vel)
        self.result_y = 2 * (self.motor1_vel + self.motor2_vel)
    
        plt.arrow(x=0,y = 0, dx = -self.motor1_vel,dy=self.motor1_vel, head_width = 0.08)
        plt.arrow(x=0,y = 0, dx = self.motor2_vel,dy = self.motor2_vel,head_width = 0.08)
        plt.arrow(x=0,y = 0, dx = -2 * self.motor3_vel, dy = self.motor3_vel,head_width = 0.1, facecolor = 'red')
        plt.arrow(x=0,y = 0, dx = 2 * self.motor4_vel, dy = self.motor4_vel, head_width = 0.1, facecolor = 'red')
        plt.arrow(x=0, y = 0, dx = self.result_x, dy = self.result_y, head_width = 0.08)

        plt.annotate('Motor 1', xy = (-self.motor1_vel / 2 + 0.25, self.motor1_vel / 2 + 0.25))
        plt.annotate('Motor 2', xy = (-self.motor1_vel / 2 + 0.25, self.motor1_vel / 2 + 0.25))
        plt.annotate('Motor 3', xy = (-self.motor1_vel / 2 + 0.25, self.motor1_vel / 2 + 0.25))
        plt.annotate('Motor 4', xy = (-self.motor1_vel / 2 + 0.25, self.motor1_vel / 2 + 0.25))

        # Create x and y axes:
        plt.axhline(y=0, color='black')
        plt.axvline(x=0, color='black')

        # Add gridlines:
        plt.grid(linestyle = '--')
        
        # Adjust the limits of the axes depending on the data:
        plt.xlim(-max(self.result_x, self.result_y) * 1.1, max(self.result_x, self.result_y) * 1.1)
        plt.ylim(-max(self.result_x, self.result_y) * 1.1 , max(self.result_x, self.result_y) * 1.1)


        # Add title and labels:
        plt.title('Macanum Wheel')

        # Add the legend for the arrows:
        plt.legend(['Motor 1', 'Motor 2', 'Motor 3', 'Motor 4', 'Resultant'])
    
        self.item1 = plt_show(plt)
    def display(self):
        return self.item1
        

def plt_show(plt, width=500, dpi=100):
    # Converts matplotlib plt to image data string
    #   plt is the matplotlib pyplot or figure
    #   width is the width of the graph image in pixels
    #   dpi (dots per inch) is the resolution of the image
    #   returns the image data string or an error message
    
    try:
        bytes = io.BytesIO()
        plt.savefig(bytes, format='png', dpi=dpi)  # Save as png image
        if hasattr(plt, "close"):
            plt.close()
        bytes.seek(0)
        base64_string = "data:image/png;base64," + \
            base64.b64encode(bytes.getvalue()).decode("utf-8")
        return "<img src='" + base64_string + "' width='" + str(width) + "'>"  # Return the image data string
    except Exception as e:
        return "<b>Exception:</b> " + str(e)  # Return the error message

def macanum_wheel(net_x, net_y):
    try:
        radians = math.atan(net_y/net_x) + 45 * (math.pi / 180)
        motor1_vel = 0 - math.cos(radians)
        motor1_x = math.tan((3 * math.pi)/ 4) * motor1_vel
        motor1_y = motor1_x
        motor2_vel = math.sin(radians)
        motor2_x = math.tan((1 * math.pi)/ 4) * motor2_vel
        motor2_y = motor2_x
        motor3_vel = motor1_vel
        motor3_x = motor1_x
        motor3_y = motor3_x
        motor4_vel = motor2_vel
        motor4_x = motor2_x
        motor4_y = motor4_x
        return [[motor1_vel, motor2_vel, motor3_vel, motor4_vel], [motor1_x,motor1_y,motor2_x,motor2_y,motor3_x,motor3_y,motor4_x,motor4_y]]



        
    except:
        if net_y > 0:
            motor1_vel = 1.0
            motor2_vel = 1.0
            motor3_vel = 1.0
            motor4_vel = 1.0
        else:
            motor1_vel = -1.0
            motor2_vel = -1.0
            motor3_vel = -1.0
            motor4_vel = -1.0

        return [motor1_vel, motor2_vel, motor3_vel, motor4_vel]



#define two arrays for plotting
def main( inputs ):

    # Create a lambda function to calculate the positioning of the labels:
    label_position = lambda y: (y * 1.1)
    
    # Get the inputs:
    a = inputs['a'] # Get the first input
    b = inputs['b'] # Get the second input
    c = inputs['c'] # Get the third input
    d = inputs['d'] # Get the fourth input
    
    # Create the plot:
    plt.xlabel('x')
    plt.ylabel('y')

    # Calculate the result vector:
    # Add the x components
    res_x = a + c
    # Add the y components
    res_y = b + d
    
    # Calculate the max number:
    try:
        max_num = max(abs(b),abs(d),abs(res_y))
    except TypeError:
        print("Invalid input")
        return
    
    # Calculate the position of the labels:
    position_index =  .1 * max_num

    # Fix the x and y axis limits
    plt.xlim(-max(abs(a),abs(c),abs(res_x)) * 1.1, max(abs(a),abs(c),abs(res_x)) * 1.1)
    plt.ylim(-max(abs(b),abs(d),abs(res_y)) * 1.1 , max(abs(b),abs(d),abs(res_y)) * 1.1)
    
    # Plot the result vector:
    plt.arrow(x = 0, y = 0, dx = inputs['a'], dy = inputs['b'], head_width = .1 * max(abs(a),abs(c),abs(res_x)), head_length = .1 * max(abs(b),abs(d),abs(res_y)), facecolor = 'blue')
    plt.arrow(x = 0, y = 0, dx = inputs['c'], dy = inputs['d'], head_width = .1 * max(abs(a),abs(c),abs(res_x)), head_length = .1 * max(abs(b),abs(d),abs(res_y)), facecolor = 'blue')
    plt.arrow(x = 0, y = 0, dx = res_x, dy = res_y, head_width = .1 * max(abs(b),abs(d),abs(res_y)), head_length = .1 * ((abs(res_x) + abs(res_y)) / 2), facecolor = 'red')
    
    plt.annotate('First vector', xy = (a/2 - 0.1,b/2 - 0.1), color = 'blue')
    plt.annotate('Second vector', xy = (c/2 - 0.1, d/2 - 0.1 ), color = 'blue')
    plt.annotate('Net vector', xy = (res_x / 2 - 0.1, res_y / 2 - 0.1), color = 'red')
    
    # Add a grid:   
    plt.grid(linestyle = '--')

    # Add a line to show the origin
    plt.axhline(y = 0, color = 'black')
    plt.axvline(x = 0, color = 'black')

    # Add a title:
    plt.title('Vector Addition')

    # Add a label to the legend:
    plt.legend(['First vector', 'Second vector', 'Net vector'], loc = 'upper right')

    #
    angle = inputs['e']
    


    # Show the plot:
    img = plt_show(plt)
    product1 = Macanum(angle)
    
    img2 = product1.display()
    

    # Return the plot:
    return {
        'plot': img,
        'Motor1': f'{(product1.motor1_vel / product1.const):.2%}',
        'Motor2': f'{(product1.motor2_vel / product1.const):.2%}',
        'Motor3': f'{(product1.motor3_vel / product1.const):.2%}',
        'Motor4': f'{(product1.motor4_vel / product1.const):.2%}',
        'item': img2

    }

# Define a function to test the main function:
def test_main(run=False):
    if run:
        # Test the main function:
        inputs = {  'a': 2, 
                    'b': 3, 
                    'c': 4, 
                    'd': 5 
                }
        try:
            # Run the main function:
            main( inputs )
         
        except Exception as e:
            # Print the error:
            print(e)

# Call the main function:
if __name__ == "__main__":
    # test the main function:
    test_main(run=False) # Set run to True to test the main function