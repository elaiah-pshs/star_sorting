# Objective: search for all variable stars in the perseus arm

# Insights:
# 1. values in data are brightness of each pixel from bottom to top, right to left
#    1st row is bottom row, first item is leftmost pixel
# 2. flood fill algorithm used to count the number of stars
# 3. algorithm can be modified to determine the position of the star in each image,
#    hence determining the position of the star in the night sky based on the image givens
#    (coords of the image, latitude and longitude taken, etc.)
# 4. algorithm can also be modified to determine the apparent magnitude of the stars by getting
#    the value of the brightest pixel and computing the magnitude from there via some
#    relation I have yet to determine (wala kasi yung data on this yung pixel brightnesses lang talaga 😭)

# TODO: get the coordinates of each star in the image and see if they are in the perseus arm (search mo na lang coords nito)

from astropy.io import fits
from FindCentre import findCentre

n_stars = 0
mapping = []
centres = []
hdul = fits.open('skv44102002825265.fits')  # open a FITS file
data = hdul[0].data  # assume the first extension is a table
for row in range(0,300):
    mapping += [[]]
    for col in range(0,300):
        if data[row][col] > 4000:
            mapping[row] += [1]
        else:
            mapping[row] += [0]

for i in range(300):
    for j in range(300):
        if mapping[i][j] == 1:
            centres.append(findCentre(mapping, data, i, j))
            n_stars += 1

print(f"Number of stars: {n_stars}")
print(f"Star coordinates on picture: {centres}")

hdul.close()
