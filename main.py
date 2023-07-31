from GenerateObjects import generateObjects
from GenerateTargets import generateTargetsByDistance
from GenerateVariables import generateVariables
from Targets import getIdByCoords, writeInfoToJson

if __name__ == "__main__":
    generateObjects("data/images/skv44513087506516_1.fits")
    generateTargetsByDistance(1950, 100)

    variable_stars = generateVariables(52.5, 45)

    for star in variable_stars:
        star_id = getIdByCoords(float(star['_RAJ2000']), float(star['_DEJ2000']))
        writeInfoToJson(star_id)
