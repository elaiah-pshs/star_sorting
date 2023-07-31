import json
from Split import split

def getIdByCoords(ra, dec):
    with open("data/objects/targets.csv", 'r') as targets:
        keys = split(targets.readline())
        ra_index = keys.index("ra")
        dec_index = keys.index("dec")

        data = list(map(split, targets.readlines()))
        min_diff = 10**6
        star_obs_id = ""

        for target in data:
            delta_ra = abs(ra - float(target[ra_index]))
            delta_dec = abs(dec - float(target[dec_index]))
            diff = (delta_ra + delta_dec) / 2

            if diff < min_diff:
                min_diff = diff
                star_obs_id = target[0]
        
        return star_obs_id

def getTargetById(star_id):
    with open("data/objects/targets.csv", 'r') as targets:
        keys = split(targets.readline())
        data = list(map(split, targets.readlines()))

        for target in data:
            if target[0] == star_id:
                return dict(zip(keys, target))

def writeInfoToJson(star_id):
    json_object = json.dumps(getTargetById(star_id), indent=4)
    with open(f"info/{star_id}.json", "w") as outfile:
        outfile.write(json_object)
