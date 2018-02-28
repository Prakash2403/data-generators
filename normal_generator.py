from pprint import pprint
import time
import numpy
import math
from uniform_generator import uniform_generator

def normal_generator():
    """ 
    Samples two independent random variables from standard Gaussian distribution.
    Uses Box-Muller Transform to generate random variables.
    Equation for Box-Muller Transform is
            Z_1 = -2log(U_1)^(1/2)*cos(2*pi*U_2)
            Z_2 = -2log(U_1)^(1/2)*sin(2*pi*U_2)
    where U_1 and U_2 are two independent random variables generated from uniform
    distribution.
    """
    uni_gen = uniform_generator()
    while True:
        u1 = next(uni_gen)
        u2 = next(uni_gen)
        if u1 == 0 or u2 == 0:
            continue
        random_number_1 = ((-2 * math.log(u1)) ** (1/2)) * math.cos(2 * math.pi * u2)
        random_number_2 = ((-2 * math.log(u1)) ** (1/2)) * math.sin(2 * math.pi * u2)  
        yield random_number_1, random_number_2


limit = 10001
if __name__ == '__main__':
    output_list = []
    print("Generating 10000 random numbers from standard normal distribution.")
    start = time.time()
    norm_gen = normal_generator()
    for i in range(10000):
       op1, op2 = next(norm_gen)
       output_list.append(op1)
       output_list.append(op2)
    end = time.time()
    print("Time taken " + str(end - start))
    print("Mean is: " + str(numpy.mean(output_list)))
    print("Standard Deviation: " + str(numpy.std(output_list)))

