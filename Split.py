def split(s):
    out = s.split(',')
    out[-1] = out[-1][:-1]
    return out
