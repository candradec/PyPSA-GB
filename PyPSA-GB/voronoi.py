"""Generates Voronoi diagram using the buses

Note that this requires specific dependencies which are probably best installed
using a virtual environment. It also takes a few minutes to run.
"""

from collections import defaultdict

import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyproj
from geovoronoi import voronoi_regions_from_coords
from geovoronoi.plotting import (plot_voronoi_polys_with_points_in_area,
                                 subplot_for_map)
from scipy.spatial import Voronoi
from shapely.geometry import Polygon

df_network = pd.read_csv("data/LOPF_data/buses.csv")
lon = df_network["x"].values
lat = df_network["y"].values
proj = pyproj.Transformer.from_crs(4326, 3857, always_xy=True)
coordinates = np.zeros(shape=(len(lon), 2))
# print(coordinates)
for i in range(len(lon)):

    coordinates[i] = proj.transform(lon[i], lat[i])

UK = gpd.read_file("UK_data/UK_shapefile/GBR_adm0.shp")
# area = world[world.name == 'United Kingdom']

UK = UK.to_crs(epsg=3857)  # convert to World Mercator CRS

# ax = UK.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
# ctx.add_basemap(ax)
# plt.show()

area_shape = UK.iloc[0].geometry  # get the Polygon

region_polys, region_pts = voronoi_regions_from_coords(
    coordinates, area_shape, per_geom=False
)

fig, ax = plt.subplots(figsize=(7, 9))
plot_voronoi_polys_with_points_in_area(
    ax,
    area_shape,
    region_polys,
    coordinates,
    region_pts,
    voronoi_and_points_cmap="tab20",
)
# ctx.add_basemap(ax)
plt.xlim([-9.29e5, 2.30e5])
plt.ylim([6.404e6, 8.134e6])
ax.axis("off")
plt.tight_layout()
plt.show()
