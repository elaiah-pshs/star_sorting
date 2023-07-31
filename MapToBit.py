def mapToBit(data, limit=0.1):
    mapping = []

    for row in range(300):
        mapping += [[]]
        for col in range(300):
            if data[row][col] > limit:
                mapping[row] += [1]
            else:
                mapping[row] += [0]

    return mapping