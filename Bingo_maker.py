# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:21:21 2016

@author: buenov
"""

import numpy as np

#INPUT FOR THE FUNCTION:
# Max Amount of numbers included
# Number of rows
# Number of columns

def grids_maker(amount_of_nb,row,column):
    #Create an array with all the numbers in random order
    array=np.arange(amount_of_nb)   
    np.random.shuffle(array)
    totalgrids=row*column
    #Make grid and put the numbers in the random order
    final_grid= array[:totalgrids].reshape((row,column))

    return final_grid
    
    
#Example:    
grids_maker(50,4,5)    
grids_maker(50,4,4)
grids_maker(50,3,3)
