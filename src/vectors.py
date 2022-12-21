import matplotlib.pyplot as plt
import numpy as np
import base64
import io


# This function is used to convert matplotlib plt to image data string:
#   plt is the matplotlib pyplot or figure
#   width is the width of the graph image in pixels
#   dpi (dots per inch) is the resolution of the image
def plt_show(plt, width=500, dpi=100):
    # Converts matplotlib plt to image data string
    #   plt is the matplotlib pyplot or figure
    #   width is the width of the graph image in pixels
    #   dpi (dots per inch) is the resolution of the image
    
    bytes = io.BytesIO()
    plt.savefig(bytes, format='png', dpi=dpi)  # Save as png image
    if hasattr(plt, "close"):
        plt.close()
    bytes.seek(0)
    base64_string = "data:image/png;base64," + \
        base64.b64encode(bytes.getvalue()).decode("utf-8")
    return "<img src='" + base64_string + "' width='" + str(width) + "'>"  # Return the image data string

#define two arrays for plotting
def main(inputs : dict):

#create scatterplot, specifying marker size to be 40
    
    '''
    num_list = [abs(inputs['a']),abs(inputs['b']),abs(inputs['c']),abs(inputs['d'])]
    max_num = max(num_list)
    '''
    # Get the inputs:
    a = inputs['a']
    b = inputs['b']
    c = inputs['c']
    d = inputs['d']
    
    # Create the plot:
    plt.xlabel('x')
    plt.ylabel('y')

    # Calculate the result vector:
    res_x = a + c
    res_y = b + d
    
    # Fix the x and y axis limits
    plt.xlim(-max(abs(a),abs(c),abs(res_x)) - 1, max(abs(a),abs(c),abs(res_x)) + 1)
    plt.ylim(-max(abs(b),abs(d),abs(res_y)) - 1, max(abs(b),abs(d),abs(res_y)) + 1)
    
    # Plot the result vector:
    plt.annotate('a + b = ' + str(res_x), xy = (0,0), xytext = (res_x + 0.25, res_y + 0.25))
    plt.annotate('c + d = ' + str(res_y), xy = (0,0), xytext = (res_x + 0.25, res_y + 0.25))
    plt.arrow(x=0, y=0, dx=inputs['a'], dy=inputs['b'], width=.08, facecolor = 'blue')
    plt.arrow(x=0, y = 0, dx = inputs['c'], dy = inputs['d'], width = .08, facecolor = 'blue')
    plt.arrow(x=0, y = 0, dx = res_x, dy = res_y, width = .08, facecolor = 'red')
    plt.annotate('First vector', xy = (a/2 - 0.1,b/2 - 0.1), color = 'blue')
    plt.annotate('Second vector', xy = (c/2 - 0.1, d/2 - 0.1 ), color = 'blue')
    plt.annotate('Net vector', xy = (res_x / 2 - 0.1, res_y / 2 - 0.1), color = 'red')
    
    '''
    plt.xticks([i * max_num for i in range(-1,2)])
    plt.yticks([i * max_num for i in range(-1,2)])
    '''
    # Add a grid:
    plt.grid(linestyle = '--')
    
    plt.legend()

    # Add a line to show the origin
    plt.axhline(y = 0, color = 'black')
    plt.axvline(x = 0, color = 'black')

#add annotation
    plt.annotate('a = ' + str(inputs['a']), xy = (0,0), xytext = (inputs['a'] + 0.25, inputs['b'] + 0.25))
    plt.annotate('b = ' + str(inputs['b']), xy = (0,0), xytext = (inputs['a'] + 0.25, inputs['b'] + 0.25))
    plt.annotate('c = ' + str(inputs['c']), xy = (0,0), xytext = (inputs['a'] + 0.25, inputs['b'] + 0.25))
    plt.annotate('d = ' + str(inputs['d']), xy = (0,0), xytext = (inputs['a'] + 0.25, inputs['b'] + 0.25))

    plt.annotate('a + c = ' + str(res_x), xy = (0,0), xytext = (res_x + 0.25, res_y + 0.25))
    plt.annotate('b + d = ' + str(res_y), xy = (0,0), xytext = (res_x + 0.25, res_y + 0.25))
    
    # Show the plot:
    img = plt_show(plt)
    # Return the plot:
    return {
        'plot': img
    }

# Call the main function:
if __name__ == "__main__":
    pass