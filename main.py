from GenerateObjects import generateObjects

if __name__ == "__main__":
    target_objects = []

    # Uncomment the line below to regenerate object list
    # generateObjects("/data/images/skv44513087506516_1.fits")

    with open("data/objects/objects.csv", 'r') as object_list:
        keys = object_list.readline().split(',')
        keys[-1] = keys[-1][:-1]
        d_index = keys.index("d")

        for line in object_list:
            values = line.split(',')
            values[-1] = values[-1][:-1]
            d = values[d_index]

            if d == "nan":
                continue
            if not 1850 < float(d) < 2050:
                continue
            else:
                target_objects.append(values)
        
    with open("data/objects/targets.csv", 'w') as target_list:
        target_list.write(','.join(keys) + '\n')
        for target in target_objects:
            target_list.write(','.join(target) + '\n')
