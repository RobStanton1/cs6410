import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt

## FUNCTION DEFINITIONS
# LOG FUNCTIONS
def log_pmf(k, p):
    # returns the pdf at k, p of the log distribution
    # as a scalar

    y = (-1/math.log(1 - p))*((p**k)/k)

    return y

def log_cdf(k, p):
    # returns the cdf for 1,..,k, and p of the log distribution
    # as a vector

    y = np.cumsum(np.array([log_pmf(k, p) for k in range(1, k + 1)]))

    return y

def log_sample(x, cdf):
    # takes a random uniform variable, x, and returns the interval index, i,
    # in which x resides, in the given cdf of the log distribution

    cdf = cdf
    count = 0

    while count < len(cdf):
        if x < cdf[count]:
            return count + 1
        else:
            count += 1
    
    return count + 1

# KUM FUNCTIONS
def kum_cdf(x, a, b):
    # returns the cdf of the kumaraswamy distribution at x
    # with parameters a and b
    
    y = 1 - (1 - x**a)**b

    return y

def kum_quantile(x, a, b):
    # takes a random uniform variable x
    # and returns the inverse cdf transform of x
    # to a random variable y that is kumaraswamy distributed
    # with parameters a, b

    y = (1-(1-x)**(1/b))**(1/a)

    return y

# PLOTTING FUNCTIONS
def cdf_plot(rand, param):
    # takes random KUM/LOG distributed numbers and plots the cdf
    # takes a parameter list of form [dist, par1, [par2]]
    n_bins = 70

    fig, ax = plt.subplots(figsize=(8, 5))

    # plot the cumulative histogram
    n, bins, patches = ax.hist(rand, n_bins, density=True, histtype='step', cumulative=True, label='Empirical')

    if(param[0] == 'KUM'):
        title = 'Kumaraswamy Distribution CDF'
        # plot the theoretical in the continous case
        x = np.linspace(0,5,num = 1000)
        ax.plot(x, kum_cdf(x, param[1], param[2]), 'k--',label = 'theoretical')

        # set appropriate limits
        ax.set_xlim(xmin = 0, xmax = 1)
        ax.set_ylim(ymin = 0, ymax = 1)

        ## TODO reconsile references to sys.argv[] and param[]
        path = sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3] + "_" + str(param[1]) + "_" + str(param[2]) + "_.pdf"

    else:
        title = 'Logarithmic Distribution CDF'

        ax.set_xlim(xmin = 0, xmax = 5)
        ax.set_ylim(ymin = 0, ymax = 1)

        path = sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3] + "_" + str(param[1]) + "_.pdf"



    # tidy up the figure
    plt.title(title)
    ax.grid(False)
    ax.legend(loc='best')

    fig.savefig(path)



def box_plot(rand, param):
    # takes random KUM/LOG distributed numbers and plots the cdf
    # takes a parameter list of form [dist, par1, [par2]]

    fig, ax = plt.subplots(figsize=(8, 5))

    # plot the cumulative histogram
    ax.boxplot(rand)

    if(param[0] == 'KUM'):
        title = 'Kumaraswamy Distribution BoxPlot'

    else:
        title = 'Logarithmic Distribution BoxPlot'



    # tidy up the figure
    plt.title(title)
    ax.grid(False)
    ax.legend(loc='best')


# INITIALISE RANDOM UNIFORM GENERATOR
# GENERATE N RANDOM UNIFORM FLOATS

try:
    n = int(sys.argv[1])
    seed = int(sys.argv[2])
    dist = sys.argv[3]

    random.seed(a = seed)
    randUnif = [random.uniform(0,1) for i in range(0, n) ]

    if (sys.argv[3] == 'KUM'):
        # KUMARASWAMY
        np.seterr(invalid='ignore')

        # assigning command line arguments to local variables
        # par1 = a and par2 = b
        a = float(sys.argv[4])
        b = float(sys.argv[5])

        try:
            # transform random uniform x into kumaraswamy distributed y,
            # with paramaters a and b, by inverse transform sampling

            randKUM = np.array([kum_quantile(i, a, b) for i in randUnif])

            # plot
            cdf_plot(randKUM, [dist, a, b])
            #box_plot(randKUM, [dist, a, b])

            #plt.show()
        except:
            print("Invalid parameter(s):")
            print("     Please enter: 0 < par1")
            print("     Please enter: 0 < par2")



    elif (sys.argv[3] == 'LOG'):
        # LOGARITHMIC
        
        # par1 = p
        p = float(sys.argv[4])
        
        try:
            # generating a logarithmic cdf
            cdf = log_cdf(5, p)
            
            # sample from log cdf with paramater p
            randLOG = np.array([log_sample(i, cdf) for i in randUnif])

            cdf_plot(randLOG, [dist, p])
            #box_plot(randLOG, [dist, p])
            
            #plt.show()
        except:
            print("Invalid parameter:")
            print("     Please enter: 0 < par1 < 1")

except:
    print("Argument Error")
    print("Please enter arguments in the following format:")
    print("     n seed dist par1 [par2]")
    print("     int: n  int: seed  str: dist  float: par1  [float: par2]")
    print("     dist IN {KUM, LOG}")