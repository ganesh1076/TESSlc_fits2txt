#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thru Jul 08 02:25:27 2021

@author: ganesh
"""
from scipy import stats
import numpy as np
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from astropy.io import ascii
from astropy.table import Table
from sys import argv, exit
import argparse
import re
import matplotlib.pyplot as plt
EXT = 1

def extract_columns_plt_pdc(fname):
    data = Table.read(fname, hdu=EXT)
    
    BJD_base = re.findall(r'\d+', str(data['TIME'].unit))[0]
    data['TIME'] = float(BJD_base) + data['TIME']
    mask = ~np.isnan(data['PDCSAP_FLUX'])
    
    datat=np.vstack((data['TIME'][mask].data,data['PDCSAP_FLUX'][mask].data, data['PDCSAP_FLUX_ERR'][mask].data))
    
    np.savetxt(fname+'_pdc.dat', datat.transpose(),delimiter='\t', fmt="%17.8f")
    
    fig = plt.figure(figsize=(10,3), tight_layout=True)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('BJD') 
    ax.set_ylabel('TESS Flux, e-/s')
    ax.plot(data['TIME'][mask].data,data['PDCSAP_FLUX'][mask].data, 'ks', ms = 1)
    plt.savefig(fname+'_pdc.pdf', dpi=(512))
    return None
    
'''    
    fig = plt.figure(figsize=(10,3), tight_layout=True)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('BJD')
    ax.set_ylabel('TESS Flux, e-/s')
    ax.errorbar(data['TIME'], data['PDCSAP_FLUX'], data['PDCSAP_FLUX_ERR'],xerr = None, capthick=0, capsize=0, ecolor='k',elinewidth=0.8, fmt="none")
'''

    


def extract_columns_plt_sap(fname):
    data = Table.read(fname, hdu=EXT)
    
    BJD_base = re.findall(r'\d+', str(data['TIME'].unit))[0]
    data['TIME'] = float(BJD_base) + data['TIME']
    mask = ~np.isnan(data['SAP_FLUX'])
    
    datat=np.vstack((data['TIME'][mask].data,data['SAP_FLUX'][mask].data, data['SAP_FLUX_ERR'][mask].data))
    
    np.savetxt(fname+'_sap.dat', datat.transpose(),delimiter='\t', fmt="%17.8f")
    
    fig = plt.figure(figsize=(10,3), tight_layout=True)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('BJD') 
    ax.set_ylabel('TESS Flux, e-/s')
    ax.plot(data['TIME'][mask].data,data['SAP_FLUX'][mask].data, 'ks', ms = 1)
    plt.savefig(fname+'_sap.pdf', dpi=(512))
    
    return None
    
    
    
if __name__ == "__main__":
    print(f"Extracting PDC_FLUX for {argv[1]}.dat")
    extract_columns_plt_pdc(argv[1])
    print(f"{argv[1]}_pdc.dat is ready")
    print(f"Extracting SAP_FLUX for {argv[1]}.dat")
    extract_columns_plt_sap(argv[1])
    print(f"{argv[1]}_sap.dat is ready")
  
  

    exit(0)
