#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created by: Ethan Lee
Email: e.lee5@newcastle.ac.uk
Date: 10/08/21
Version: 1.0

Changes by versions: 
    1.0: Code runs 

Remember that all the rasters within the folder MUST BE IN THE SAME PROJECTION
otherwise the merge will not be correctly formated.
'''

import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os
from osgeo import gdal

dirpath = r"C:/Users/ethan.lee1/Documents/Mitacs_project/Original Data/RGI1/Ice_thickness/Resample/"

out_fp = r"C:/Users/ethan.lee1/Documents/Mitacs_project/Original Data/RGI1/Ice_thickness/Merged/ice_thk_merged.tif"

search_criteria = "RGI*.tif"

q = os.path.join(dirpath, search_criteria)

print(q)

thk_fps = glob.glob(q)

print(thk_fps)

src_files_to_mosaic = []

for fp in thk_fps:
    src = rasterio.open(fp)
    src_files_to_mosaic.append(src)
    
src_files_to_mosaic

mosaic, out_trans = merge(src_files_to_mosaic, method='max')

out_meta = src.meta.copy()

out_meta.update({"driver": "GTiff",
                 "height": mosaic.shape[1],
                 "width": mosaic.shape[2],
                 "transform": out_trans,
                 "crs": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs "
                 }
                )

with rasterio.open(out_fp, "w", **out_meta) as dest:
    dest.write(mosaic)
    
print('Merged Finished')