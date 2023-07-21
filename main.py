# Objective:
# -     search for all variable stars in the perseus arm

# Insights:
# 1.    values in data are brightness of each pixel from bottom to top, right
#       to left; 1st row is bottom row, first item is leftmost pixel (i.e.,
#       bottom left point is the origin)
# 2.    flood fill algorithm used to count the number of stars
# 3.    algorithm can be modified to determine the position of the star in each
#       image, hence determining the position of the star in the night sky
#       based on the image givens (coords of the image, lat & long taken, etc.)
# 4.    algorithm can also be modified to determine the apparent magnitude of
#       the stars by getting the value of the brightest pixel and computing the
#       magnitude from there via some relation that has yet to be determined

# TODO: get the coordinates of each star in the image and see if they are in
#       the perseus arm

from astropy.io import fits
from astropy.wcs import WCS
from FindCentre import findCentre

mapping = []
centres = []
hdul = fits.open('skv44102002825265.fits')  # open a FITS file
w = WCS(hdul[0].header)
data = hdul[0].data  # assume the first extension is a table
for row in range(0,300):
    mapping += [[]]
    for col in range(0,300):
        if data[row][col] > 4000:
            mapping[row] += [1]
        else:
            mapping[row] += [0]

for row in range(300):
    for col in range(300):
        if mapping[row][col] == 1:
            centres.append(w.pixel_to_world(*findCentre(mapping, data, row, col)))

print(f"Equatorial coordinates of first star: {centres[0]}")

hdul.close()
