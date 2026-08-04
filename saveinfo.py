# saving important information from the runs used for checking that they're working as expected
# specifically, this looks like a timeseries file of average properties at the surface and 50 m
# in the analysis boxes, for temperature, salinity, oxygen, DIC, TA, nitrogen
# seperate dataframe for each year, region, and depth division
print('start')

import argparse
from pathlib import Path
import xarray as xr
import numpy as np
import pandas as pd

# allow folder (ie. change scenario applied and year) to be input in the command line
# e.g. pixi run -e default python saveinfo.py "All" 2018
parser = argparse.ArgumentParser(description='Get folder/scenario name.')
parser.add_argument('scenario', type=str,
                    help='scenario - use spelling from folder name')
parser.add_argument('year', type=int,
                    help='run year')
args = parser.parse_args()

scenario = args.scenario
year = args.year

# booleans describing the different regions of analysis
def booleans(mydata,region,depth):

    if depth==50:
        depth_bool = (mydata.deptht>40) & (mydata.deptht<60)
    elif depth==300:
        depth_bool = (mydata.deptht>290) & (mydata.deptht<310)


    # region can be jdf, pug (puget sound), nsg (northern SoG), and csg (central SoG)
    # based on boxes on map
    if region == 'jdf':
        y_bool = (mydata.y >=310) & (mydata.y <360) 
        x_bool = (mydata.x >=50) & (mydata.x<100)
    
    elif region == 'pug':
        y_bool = (mydata.y >=80) & (mydata.y <130)
        x_bool = (mydata.x >=220) & (mydata.x<270)

    elif region == 'nsg':
        y_bool = (mydata.y >=650) & (mydata.y <700)
        x_bool = (mydata.x >=130) & (mydata.x<180)

    elif region == 'csg':
        y_bool = (mydata.y >=460) & (mydata.y <510)
        x_bool = (mydata.x >=240) & (mydata.x<290)

    else:
        print("invalid region name")

    return depth_bool, y_bool, x_bool


# import data
path = Path(f"/scratch/rbeutel/MEOPAR/results/{scenario}Change_{year}_spin")
bath = xr.open_dataset("/home/rbeutel/MEOPAR/grid/bathymetry_202108.nc") # bathymetry for masking land values
data = xr.open_mfdataset(sorted(path.glob(f"SalishSea_1d_{year}0101_{year}1231_pri_T_{year}*.nc"))).where(~np.isnan(bath.Bathymetry))
print('import done')

# setup dataframe
days = np.array(pd.to_datetime(data.time_counter.values))
filler = np.empty(len(days))
d = {'date':days,'temp':filler,'salt':filler,'DO':filler,'DIC':filler,'TA':filler,'NO3':filler}


# jdf 50 m
depth_bool, y_bool, x_bool = booleans(data,'jdf',depth=50)
df = pd.DataFrame(d)
df['temp'] = np.mean(data.votemper[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['salt'] = np.mean(data.vosaline[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DO'] = np.mean(data.dissolved_oxygen[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DIC'] = np.mean(data.dissolved_inorganic_carbon[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['TA'] = np.mean(data.total_alkalinity[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['NO3'] = np.mean(data.nitrate[:,depth_bool,y_bool,x_bool],axis=(1,2,3))

df.to_csv(f"./output/jdf_50m_{scenario}{year}_spin")
print(f"./output/jdf_50m_{scenario}{year}_spin")


# pug 50 m
depth_bool, y_bool, x_bool = booleans(data,'pug',depth=50)
df = pd.DataFrame(d)
df['temp'] = np.mean(data.votemper[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['salt'] = np.mean(data.vosaline[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DO'] = np.mean(data.dissolved_oxygen[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DIC'] = np.mean(data.dissolved_inorganic_carbon[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['TA'] = np.mean(data.total_alkalinity[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['NO3'] = np.mean(data.nitrate[:,depth_bool,y_bool,x_bool],axis=(1,2,3))

df.to_csv(f"./output/pug_50m_{scenario}{year}_spin")
print(f"./output/pug_50m_{scenario}{year}_spin")


# nsg 50 m
depth_bool, y_bool, x_bool = booleans(data,'nsg',depth=50)
df = pd.DataFrame(d)
df['temp'] = np.mean(data.votemper[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['salt'] = np.mean(data.vosaline[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DO'] = np.mean(data.dissolved_oxygen[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DIC'] = np.mean(data.dissolved_inorganic_carbon[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['TA'] = np.mean(data.total_alkalinity[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['NO3'] = np.mean(data.nitrate[:,depth_bool,y_bool,x_bool],axis=(1,2,3))

df.to_csv(f"./output/nsg_50m_{scenario}{year}_spin")
print(f"./output/nsg_50m_{scenario}{year}_spin")


# csg 50 m
depth_bool, y_bool, x_bool = booleans(data,'csg',depth=50)
df = pd.DataFrame(d)
df['temp'] = np.mean(data.votemper[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['salt'] = np.mean(data.vosaline[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DO'] = np.mean(data.dissolved_oxygen[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DIC'] = np.mean(data.dissolved_inorganic_carbon[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['TA'] = np.mean(data.total_alkalinity[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['NO3'] = np.mean(data.nitrate[:,depth_bool,y_bool,x_bool],axis=(1,2,3))

df.to_csv(f"./output/csg_50m_{scenario}{year}_spin")
print(f"./output/csg_50m_{scenario}{year}_spin")

# csg deep
depth_bool, y_bool, x_bool = booleans(data,'csg',depth=300)
df = pd.DataFrame(d)
df['temp'] = np.mean(data.votemper[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['salt'] = np.mean(data.vosaline[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DO'] = np.mean(data.dissolved_oxygen[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['DIC'] = np.mean(data.dissolved_inorganic_carbon[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['TA'] = np.mean(data.total_alkalinity[:,depth_bool,y_bool,x_bool],axis=(1,2,3))
df['NO3'] = np.mean(data.nitrate[:,depth_bool,y_bool,x_bool],axis=(1,2,3))

df.to_csv(f"./output/csg_deep_{scenario}{year}_spin")
print(f"./output/csg_deep_{scenario}{year}_spin")
