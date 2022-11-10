#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by: Ethan Lee
Email: e.lee5@newcastle.ac.uk
Date: 10/08/21
Version: 1.0

Changes by versions: 
    1.0: Code runs 

This script reprojects the Faritnotti et al. (2019) ice thickness data
due to the inidivdual rasters being within differing UTM zones

"""

import rasterio, os
from rasterio.warp import calculate_default_transform, reproject, Resampling

# the CRS you would like to reproject them into (need the EPSG code)
dstCrs = {'init':'EPSG:4326'} #WGS_84

# the location where the rasters are saved
srcPath = "C:/Users/ethan.lee1/Documents/Mitacs_project/Original Data/RGI1/Ice_thickness/Original/"

# places all file names with the file type .tif into a list
lstRst = [r for r in os.listdir(srcPath) if r.endswith('tif')]
lstRst

# combines the file path and name to know that CRS it is
expRst = rasterio.open(srcPath+lstRst[0])
expRst.crs

# the destination path for the output rasters
dstPath = 'C:/Users/ethan.lee1/Documents/Mitacs_project/Original Data/RGI1/Ice_thickness/Reproject/'

# how the rasters are reprojected
def reprojectRaster(srcRst, dstRst, dstCrs, srcPath, dstPath):
    srcRst = rasterio.open(srcPath+srcRst)
    
    transform, width, height = calculate_default_transform(
        srcRst.crs, dstCrs, srcRst.width, srcRst.height, *srcRst.bounds)
    
    kwargs = srcRst.meta.copy()
    kwargs.update({
        'crs': dstCrs,
        'transform': transform,
        'width': width,
        'height': height,
        })
    
    dstRst = rasterio.open(dstPath+dstRst, 'w', **kwargs)
    
    for i in range (1, srcRst.count + 1):
        reproject(
            source = rasterio.band(srcRst, i),
            destination = rasterio.band(dstRst, i),
            src_crs = srcRst.crs,
            dst_crs = dstCrs,
            resampling = Resampling.cubic)
        
    dstRst.close()

# saves the now reprojected rasters
for srcRst in lstRst:
    dstRst = srcRst[:-4]+'_WGS_84'+srcRst[-4:]
    reprojectRaster(srcRst, dstRst, dstCrs, srcPath, dstPath)
    print('Reprojection of %s done' %srcRst)
    
print('Reprojections complete')