import os
from more_itertools import unique_everseen
from astropy.io import fits
from astropy.wcs import WCS
from astropy.table import hstack, vstack
from astroquery.mast import Catalogs
from FindCentre import findCentre

mapping = []
objects = []

hdul = fits.open('./data/images/skv44513087506516_1.fits')  # open a FITS file
w = WCS(hdul[0].header)

data = hdul[0].data  # assume the first extension is a table
for row in range(300):
    mapping += [[]]
    for col in range(300):
        if data[row][col] > 0.1:
            mapping[row] += [1]
        else:
            mapping[row] += [0]

for row in range(300):
    for col in range(300):
        if mapping[row][col] == 1:
            coords = w.pixel_to_world(*findCentre(mapping, data, row, col))
            obs_table = Catalogs.query_criteria(
                coordinates=coords.to_string(),
                catalog="Tic",
                objType="STAR"
            )
            objects.append(hstack(obs_table))
            print(f"LOG: Added stars from query centered around coordinates {coords.to_string()}")

objects = vstack(objects)
objects.write("./data/objects/temp.csv", format='ascii.csv', overwrite=True)

with open('./data/objects/temp.csv', 'r') as f, open('./data/objects/objects.csv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))

os.remove("./data/objects/temp.csv")

hdul.close()
