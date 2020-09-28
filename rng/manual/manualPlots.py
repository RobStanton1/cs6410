import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as special
import scipy.integrate as integrate

## this script produces theoretical cdf/pdf plots for both the kumaraswamy
## and Logarithmic distributions

## These plots are used in part one of the manaul
    
def kum_pdf(x, a, b):
    # returns the pdf of the kumaraswamy distribution at x
    # with parameters a and b
    
    y = a*b*x**(a-1)*(1 - x**a)**(b-1)
    
    return y


def kum_cdf(x, a, b):
    # returns the cdf of the kumaraswamy distribution at x
    # with parameters a and b
    
    y = 1 - (1 - x**a)**b

    return y 
   
def log_pmf(k, p):
    # returns the pdf at k, p of the log distribution
    # as a scalar

    y = (-1/math.log(1 - p))*((p**k)/k)

    return y

def log_pmf_vector(k, p):
    # returns the pdf at k, p of the log distribution
    # as a vector (used for generating pmf plots in a similar manner to the cdf)

    y = np.array([(-1/math.log(1 - p))*((p**k)/k) for k in range(1, k + 1)])

    return y

def log_cdf(k, p):
    # returns the cdf for 1,..,k, and p of the log distribution
    # as a vector

    y = np.cumsum(np.array([log_pmf(k, p) for k in range(1, k + 1)]))

    return y
    
def log_cdf_plot(p):
    # this function plots the cdf
    # of the logarithmic distribution
    # for several values of p
    
    # create a plot etc
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # a series of log_cdf arrays
    log_cdf_array = [log_cdf(5, i) for i in p]
    
    x = np.linspace(1, 5, num = 1000)
    style = ['k-', 'k--', 'k-.']
    labels = ['p =' + str(i) for i in p]
    
    
    count = 0
    
    while(count < len(log_cdf_array)):
        ax.plot(x, [log_cdf_array[count][math.floor(i)-1] for i in x], style[count], label = labels[count])
        count += 1
        
    plt.title('Logarithmic distribution CDF')
    ax.grid(False)
    ax.set_xlim(xmin = 0, xmax = 5)
    ax.set_ylim(ymin = 0, ymax = 1)
    legend = ax.legend(loc='best', fontsize=14)
    
    fig.savefig('log_cdf.pdf')

def log_pmf_plot(p):
    # this function plots the cdf
    # of the logarithmic distribution
    # for several values of p
    
    # create a plot etc
    fig, ax = plt.subplots(figsize=(8, 5))
    
    #  a series of log_pdf arrays
    log_pmf_array = [log_pmf_vector(5, i) for i in p]
    
    x = [1,2,3,4,5]
    y = [0,1,2,3,4]
    style = ['sk-', 'ok--', '^k-.']
    labels = ['p =' + str(i) for i in p]
    
    
    count = 0
    
    while(count < len(log_pmf_array)):
        ax.plot(x, [log_pmf_array[count][i] for i in y], style[count], label = labels[count])
        count += 1
    
    plt.title('Logarithmic distribution PMF')
    ax.grid(False)
    ax.set_xlim(xmin = 0, xmax = 5)
    ax.set_ylim(ymin = 0, ymax = 1)
    legend = ax.legend(loc='best', fontsize=14)
    
    fig.savefig('log_pmf.pdf')
    
def kum_cdf_plot(a, b):
    # this function plots the cdf
    # of the kumaraswamy distribution
    # for several values of a, b
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    x = np.linspace(0, 1, num = 1000)
    style = style = ['k-', 'k--', 'k-.', 'k:']
    labels = [[r'$\alpha = $' + str(i) + ', ' for i in a][i] + [r'$\beta = $' + str(j) for j in b][i] for i in range(0, len(a))]
    
    count = 0
    
    while(count < len(a)):
        ax.plot(x, kum_cdf(x, a[count], b[count]), style[count], label = labels[count])
        count += 1
    
    plt.title('Kumaraswamy distribution CDF')
    ax.grid(False)
    ax.set_xlim(xmin = 0, xmax = 1)
    ax.set_ylim(ymin = 0, ymax = 1)
    legend = ax.legend(loc='best', fontsize=14)
    
    fig.savefig('kum_cdf.pdf')


def kum_pdf_plot(a, b):
    # this function plots the pdf
    # of the kumaraswamy distribution
    # for several values of a, b
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    x = np.linspace(0, 1, num = 1000)
    style = style = ['k-', 'k--', 'k-.', 'k:']
    labels = [[r'$\alpha = $' + str(i) + ', ' for i in a][i] + [r'$\beta = $' + str(j) for j in b][i] for i in range(0, len(a))]
    
    count = 0
    
    while(count < len(a)):
        ax.plot(x, kum_pdf(x, a[count], b[count]), style[count], label = labels[count])
        count += 1
    
    plt.title('Kumaraswamy distribution PDF')
    ax.grid(False)
    ax.set_xlim(xmin = 0, xmax = 1)
    ax.set_ylim(ymin = 0, ymax = 3)
    legend = ax.legend(loc='best', fontsize=14)
    
    fig.savefig('kum_pdf.pdf')
    
p = [0.33, 0.66, 0.99]
log_cdf_plot(p)
log_pmf_plot(p)

a = [0.5, 5.0, 1.0, 2.0]
b = [0.5, 1.0, 3.0, 5.0]
kum_cdf_plot(a, b)
kum_pdf_plot(a, b)

