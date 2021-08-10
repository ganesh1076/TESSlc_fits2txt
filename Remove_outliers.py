#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 23:41:26 2020

@author: ganesh
"""
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from astropy.timeseries import LombScargle
from sys import argv, exit
import matplotlib as mpl

fontsize = 11

mpl.rcParams['xtick.labelsize'] = fontsize
mpl.rcParams['ytick.labelsize'] = fontsize
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times Palatino, New Century Schoolbook, Bookman,  Computer Modern Roman'
mpl.rcParams['text.usetex'] = True


def Remove_outliers(t,f,ferr):
	'''To remove the outliers or jumps in the data'''
    t1=[]
    f1=[]
    ferr1=[]
    sd=np.abs(stats.zscore(f))
    
    for i in range(len(f)):
        if sd[i]<=3:
            f1.append(f[i])
            t1.append(t[i])
            ferr1.append(ferr[i])
        
    np.savetxt(argv[1]+'_rmot.dat',np.column_stack((t1,f1, ferr1)),newline= '\n',delimiter='\t', fmt="%17.8f")
#figure

'''
import lightkurve as lkc

lc =lkc.LightCurve(time=data[0],flux=data[1],flux_err=data[2])
lc_clean = lc.remove_outliers(sigma=3)
plt.plot(lc_clean.time.value,lc_clean.flux.value, 'ks', ms=2)
plt.show()


'''


    m1=-2.5*np.log10(f1)
    mag=m1
    m=np.mean(mag)
    del_mag=(mag-m)*1000
    JD_base=t1[0]

    plt.figure(figsize=(10,3), constrained_layout=True)
    ax1=plt.subplot(1,1,1)
    ax1.set(title='Lightcurve')
    ax1.set_xlabel(f"BJD, {JD_base}+")
    ax1.set_ylabel('Delta mmag')
    # plt.annotate('Sec-7', (4,0.5))
    ax1.invert_yaxis()
    ax1.plot(t1-JD_base,del_mag,'ks', ms=1)
    #plt.show()
    #plt.savefig('figure_lc.pdf', dpi=(512))
    plt.savefig(argv[1]+'lc.pdf', dpi=(512))
    
        
if __name__ == "__main__":
    t, f, ferr = np.loadtxt(argv[1], unpack=True, usecols=(0,1,2), comments='#')
    Remove_outliers(t,f,ferr)
    
    exit(0)
     

    
    
