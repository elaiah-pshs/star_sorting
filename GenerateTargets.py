from Split import split

def generateTargetsByDistance(target, margin, objects="data/objects/objects.csv", out_name="targets"):
    target_objects = []

    with open(objects, 'r') as object_list:
        keys = split(object_list.readline())
        d_index = keys.index("d")

        for line in object_list:
            values = split(line)
            d = values[d_index]

            if d == "nan":
                continue
            if not target - margin < float(d) < target + margin:
                continue
            else:
                target_objects.append(values)
        
    with open(f"data/objects/{out_name}.csv", 'w') as target_list:
        target_list.write(','.join(keys) + '\n')
        for target in target_objects:
            target_list.write(','.join(target) + '\n')
