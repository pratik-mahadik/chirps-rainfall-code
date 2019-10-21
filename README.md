# chirps-rainfall-code
Code to unzip and clip chirps 5km x 5km rainfall data

Climate Hazards Group InfraRed Precipitation with Station data (CHIRPS) is a 35+ year quasi-global rainfall data set. Spanning 50°S-50°N (and all longitudes) and ranging from 1981 to near-present, CHIRPS incorporates our in-house climatology, CHPclim, 0.05° resolution satellite imagery, and in-situ station data to create gridded rainfall time series for trend analysis and seasonal drought monitoring. 

Read more about CHIRPS here: https://www.nature.com/articles/sdata201566
 
Access CHIRPS using folowing links:

ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRPS-2.0

https://clim-engine-development.appspot.com/fewsNet

https://climateserv.servirglobal.net/

https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_DAILY

https://developers.google.com/earth-engine/datasets/catalog/UCSB-CHG_CHIRPS_PENTAD

https://earlywarning.usgs.gov/fews/ewx/index.html

The python code uses gzip library of python to unzip the product which is in *.tar.xz* extension.

Then gdal cli command was use to clip chirps world view data to data as per area of interest.
