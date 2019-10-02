d = {}
def update_dictionary(d, key, value):
    if key in d:
        d[key] = value
    if key not in d:
        d[key*2] = value
    if key*2 not in d:
        d[2*key] = value