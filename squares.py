import math
def squares(n):
    '''return a list of square numbers less than n'''
    sqr = [i*i for i in range(1,math.ceil(n**0.5))]
    return sqr