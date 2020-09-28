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

def log_theoretical(p):
    # This function is an alternative method of plotting the
    # cdf of the logarithmic distribution.
    
    # This function performs the exact same operations as those
    # found in the logarithmic branch of the cdf_plot function.
    # However, for accuracy, this function performms 10000 samples.
      
    # The theoretical log cdf is implemented in this way as an alternative
    # to programming the incomplete beta function.

    # This function returns a series of logarithmic distributed random variates with paramater p

    return np.array([log_sample(x, log_cdf(6, p)) for x in [random.uniform(0,1) for i in range(0,10000)]])

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
def cdf_plot(rand):
    # takes random KUM/LOG distributed numbers and plots the cdf
    n_bins = 70

    fig, ax = plt.subplots(figsize=(8, 5))

    # plot the cumulative histogram
    n, bins, patches = ax.hist(rand, n_bins, density=True, histtype='step', cumulative=True, label='Empirical')

    if(sys.argv[3].lower() == 'kum'):

        title = 'Kumaraswamy Distribution CDF'

        # plot the theoretical`
        x = np.linspace(0,1,num = 1000)
        ax.plot(x, kum_cdf(x, float(sys.argv[4]), float(sys.argv[5])), 'k--',label = 'theoretical')

        # set appropriate limits
        ax.set_xlim(xmin = 0, xmax = 1)
        ax.set_ylim(ymin = 0, ymax = 1)

        path = sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3].upper() + "_" + sys.argv[4] + "_" + sys.argv[5] + "_cdf_.pdf"

    elif(sys.argv[3].lower() == 'log'):

        title = 'Logarithmic Distribution CDF'

        #  plot the theoretical
        ax.hist(log_theoretical(float(sys.argv[4])), n_bins, density=True, histtype='step', cumulative=True, label='Theoretical')

        # set appropriate limits
        ax.set_xlim(xmin = 0, xmax = 5)
        ax.set_ylim(ymin = 0, ymax = 1)

        path = sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3].upper() + "_" + sys.argv[4] + "_cdf_.pdf"



    # tidy up the figure
    plt.title(title)
    ax.grid(False)
    ax.legend(loc='best')

    fig.savefig(path)



def box_plot(rand):
    # takes random KUM/LOG distributed numbers and plots the cdf
    # takes a parameter list of form [dist, par1, [par2]]

    fig, ax = plt.subplots(figsize=(8, 5))

    # plot the cumulative histogram
    ax.boxplot(rand)

    if(sys.argv[3].lower() == 'kum'):
        title = 'Kumaraswamy Distribution BoxPlot'

    elif(sys.argv[3].lower() == 'log'):
        title = 'Logarithmic Distribution BoxPlot'



    # tidy up the figure
    plt.title(title)
    ax.grid(False)
    ax.legend(loc='best')


def export_sequences(rand):
    # this function takes a random sequence and
    # creates two output files
    # the first file contains the sequence
    # the second file contains an evaluation of the cdf
    # for various values of x. This second file is independent of
    # the input rand.

    if(sys.argv[3].lower() == 'kum'):

        # print generated sequence rand to file

        seqPath = sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3].upper() + "_" + sys.argv[4] + "_" + sys.argv[5] + "_seq_.txt"
        sequenceExport = open(seqPath, 'w')
        
        for variate in rand:
            print(variate, file = sequenceExport)

        sequenceExport.close()

        # print an evaluation of the kumaraswamy cdf for 1000 values between [0,1] to file

        x = np.linspace(0,1,num = 1000)

        cdfDataPath = sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3].upper() + "_" + sys.argv[4] + "_" + sys.argv[5] + "_cdfData_.txt"
        cdfDataExport = open(cdfDataPath, "w")

        for i in x:
            print(i,",", kum_cdf(x, float(sys.argv[4]), float(sys.argv[5])), file = cdfDataExport)

        cdfDataExport.close()



    elif(sys.argv[3].lower() == 'log'):

        path = sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3].upper() + "_" + sys.argv[4] + "_seq_.txt"
    




# INITIALISE RANDOM UNIFORM GENERATOR
# GENERATE N RANDOM UNIFORM FLOATS

try:
    n = int(sys.argv[1])
    seed = int(sys.argv[2])
    dist = sys.argv[3]

    random.seed(a = seed)
    randUnif = [random.uniform(0,1) for i in range(0, n) ]

    if (sys.argv[3].lower() == 'kum'):
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
            cdf_plot(randKUM)
            #box_plot(randKUM)

            #plt.show()

        except:
            print("Invalid parameter(s):")
            print("     Please enter: 0 < par1")
            print("     Please enter: 0 < par2")



    elif (sys.argv[3].lower() == 'log'):
        # LOGARITHMIC
        
        # par1 = p
        p = float(sys.argv[4])
        
        try:
            # generating a logarithmic cdf
            cdf = log_cdf(6, p)
            print(cdf)
            
            # sample from log cdf with paramater p
            randLOG = np.array([log_sample(i, cdf) for i in randUnif])

            cdf_plot(randLOG)
            #box_plot(randLOG)
            
            #plt.show()

        except:
            print("Invalid parameter:")
            print("     Please enter: 0 < par1 < 1")

    else:
        print("Please enter valid distribtion:")
        print("     dist IN {KUM, LOG}")

except:
    print("Argument Error")
    print("Please enter arguments in the following format:")
    print("     n seed dist par1 [par2]")
    print("     int: n  int: seed  str: dist  float: par1  [float: par2]")
    print("     dist IN {KUM, LOG}")