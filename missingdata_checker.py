# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:33:59 2016

@author: buenov
"""


from __future__ import division
import matplotlib.pyplot as plt
    

## Check the percentage of missing data using the input file for STRUCTURE

f=open('Structure_syn_all_data_biallelic_flip.str')


test = f.readline()
markers = test.split()

percentages={}
perc_distribution=[]

for line in f:
    bits = line.split()
    library = bits[0]
    bases=bits[1:]
    missing_data=0
    
    #Get the count of missing data per library and save it
    for base in bases:
        if str(base)=='-9':
            missing_data+=1 

    perc_missing=missing_data/len(bases)
    
    perc_distribution.append(perc_missing*100)
    percentages[library]=perc_missing
    
# Plot the distribution of percentages of missing data
    
n, bins, patches = plt.hist(perc_distribution,50,normed=1,facecolor='b')

#Number of libraries with a lot of missing data
low_quality=[]
for lib in percentages:
    if percentages[lib] > 0.7 :
        low_quality.append(lib)
len(low_quality)/2

#Number of libraries with low missing data
high_quality=[]
for lib in percentages:
    if percentages[lib] < 0.3 :
        high_quality.append(lib)
len(high_quality)/2
