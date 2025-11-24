import math
import numpy as np

# Define your new functions below
def mean(x):
    sum(mean)


def gaussian(x, mean, stddev):
    """
    Compute the Gaussian (Normal) probability density function.
    
    Parameters:
        x (float): The point at which to evaluate the PDF
        mean (float): Mean of the distribution
        stddev (float): Standard deviation of the distribution

    Returns:
        float: The probability density function value at x
    """
    x = np.array(x, dtype=np.float64)
    mean = np.array(mean, dtype=np.float64)
    stddev = np.array(stddev, dtype=np.float64)
    
    coefficient = 1 / (stddev * np.sqrt(2 * np.pi))
    exponent = -((x - mean) ** 2) / (2 * stddev ** 2)
    return coefficient * np.exp(exponent)
    

