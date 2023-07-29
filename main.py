# Objective:
# -     search for all variable stars in the perseus arm

# TODO: get the coordinates of each star in the image and see if they are in
#       the perseus arm

from astropy.io import fits
from astropy.wcs import WCS
from astroquery.mast import Observations
from FindCentre import findCentre

mapping = []
centres = []

hdul = fits.open('skv44513087506516_1.fits')  # open a FITS file
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
            # centres.append(findCentre(mapping, data, row, col))
            centres.append(w.pixel_to_world(
                *findCentre(mapping, data, row, col)
            ))

obs_table = Observations.query_region(centres[0])
print(obs_table)
print(centres)

hdul.close()
