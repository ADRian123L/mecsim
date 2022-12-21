import matplotlib.pyplot as plt
import numpy as np
import base64
import io

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
    return "<img src='" + base64_string + "' width='" + str(width) + "'>"


#define two arrays for plotting
def main(inputs):
    

#create scatterplot, specifying marker size to be 40
    
    '''
    num_list = [abs(inputs['a']),abs(inputs['b']),abs(inputs['c']),abs(inputs['d'])]
    max_num = max(num_list)
    '''
    a = inputs['a']
    b = inputs['b']
    c = inputs['c']
    d = inputs['d']
    
    plt.xlabel('x')
    plt.ylabel('y')

    res_x = a + c
    res_y = b + d
    
    
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
    plt.grid(linestyle = '--')
    
    plt.legend()

#add annotation
    

   
    img = plt_show(plt)
    return {
        'plot': img
    }
    
