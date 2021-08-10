# TESSlc_fits2txt

#A python code to convert fits into dat for TESS light curves data
#<fname>_pdc.dat is for PDC_FLUX
#<fname>_sap.dat is for SAP_FLUX
  
  #To Run the code:
  #enter the following line in the terminal which contains the TESS data
  "python tess_extract_pdc_sap.py <TESS_lightcurve_file.fits>

  
  
  
  #Remove Outlier
  
  It can be used after extracting the data in .dat file even though it is SAP or PDC flux, the code will try to find the outliers and remove those values whcih are sigma>3. 
