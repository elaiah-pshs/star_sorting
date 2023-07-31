import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.vizier import Vizier

def generateVariables(centre_ra, centre_dec, w=30):
    # Query the Variable Star Index (VSX) catalog from Vizier
    v = Vizier(columns=['_RAJ2000', '_DEJ2000','B-V', 'Vmag', 'Plx', 'Type'],
            keywords=["optical"], catalog='B/vsx/vsx')
    coord = SkyCoord(ra=centre_ra, dec=centre_dec, unit=(u.deg, u.deg), frame='icrs')
    result = v.query_region(coord, width=w*u.arcmin)

    variable_stars = []

    for i in result[0]:
        if i['Type'] == "VAR":
            variable_stars.append(i)

    return variable_stars
