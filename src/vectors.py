import matplotlib.pyplot as plt
import numpy as np
import base64
import io
import os
from PIL import Image
import math


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
        base64_string = "data:image/png;base64," + base64.b64encode(bytes.getvalue()).decode("utf-8")
        return "<img src='" + base64_string + "' width='" + str(width) + "'>"  # Return the image data string
    except Exception as e:
        return "<b>Exception:</b> " + str(e)  # Return the error message

def macanum_wheel(net_x, net_y):
    try:
        radians = math.atan(net_y/net_x) - 45 * (math.pi / 180)
        motor1_vel = 0 - math.sin(radians)
        motor2_vel = math.cos(radians)
        motor3_vel = motor1_vel
        motor4_vel = motor2_vel
        return [motor1_vel, motor2_vel, motor3_vel, motor4_vel]
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

    # Show the plot:
    img = plt_show(plt)
    

    # Return the plot:
    return {
        'plot': img,
        'Motor1': f'{macanum_wheel(res_x, res_y)[0]:.2%}',
        'Motor2': f'{macanum_wheel(res_x, res_y)[1]:.2%}',
        'Motor3': f'{macanum_wheel(res_x, res_y)[2]:.2%}',
        'Motor4': f'{macanum_wheel(res_x, res_y)[3]:.2%}'

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
