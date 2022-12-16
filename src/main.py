"""
    The code drives a website in Mecsim.
"""

from math import pi, sin, cos

def main(inputs : dict) -> dict:
    """The function returns a dictionary with the 
    response to the inputs."""
    # Inputs:z
    radian = ((pi / 180) * (inputs['angle'] + 45))
    # Calls the function:
    vectors = vector(radian)
    # Returns a dictionary with the outputs:
    return {
        "angle": inputs['angle'],
        "number_1": vectors[0],
        "number_2": vectors[1],
        "number_3": vectors[2],
        "number_4": vectors[3]
    }

def vector(radian : float) -> list:
    """The function return a list with the vectors for
    controlling a vehicle."""
    # Converts to x - y components:
    x_comp = cos(radian)
    y_comp = sin(radian)
# Creates a list:
    vectors = [-x_comp, y_comp, -x_comp, y_comp]
    new_vector = list()
    # Changes the floats into integers:
    for i in vectors[:]:
        nums = round(i)
        new_vector.append(nums)
    return new_vector

inputs = {'angle' : 90}
print(main(inputs))