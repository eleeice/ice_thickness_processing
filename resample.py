#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by: Ethan Lee
Email: e.lee5@newcastle.ac.uk
Date: 10/08/21
Version: 1.0

Changes by versions: 
    1.0: Code runs 

This script is to take in the reprojected Faritnotti et al. (2019) ice
thicknesses, and resampls them to 30 m using a cubic resampling method.

"""

from osgeo import gdal
import os

# directs where the rasters are
srcPath = 'C:/Users/ethan.lee1/Documents/Mitacs_project/Original Data/RGI1/Ice_thickness/Reproject/' 

# creates a list of all rasters that have the file type .tif
lstRst = [r for r in os.listdir(srcPath) if r.endswith('.tif')] 
lstRst

# the location where they are to be saved
dstPath = 'C:/Users/ethan.lee1/Documents/Mitacs_project/Original Data/RGI1/Ice_thickness/Resample/' 

# the resampling of the raster to 30 m resolution using the cubic resampling method
def resample(srcRst, dstRst):
    dsresamp = gdal.Warp(dstRst, srcRst, xRes = 0.0002777777777777777775, yRes = 0.0002777777777777777775, resampleAlg = "cubic")
    dsresamp = None

# iterates through the list (lstRst) and resamples the rasters individually
for srcRst in lstRst:
    ds = gdal.Open(srcPath+srcRst)
    dstRst = dstPath+srcRst[:-4]+'_resampled'+srcRst[-4:]
    resample(ds, dstRst)
    print('%s Resampled' %srcRst)
    
print('\nResampling completed')
