
def geoTuple(geos):
    return [(float(geo[0]), float(geo[1])) for geo in [g.split(",") for g in geos]]









geos = ["-42.94284,72.8923840", "-42.942543684,72.8324923840", "-42.93463298504284,72.8924363438850293850923540", "-42.4594284,72.8964323840"]

print(*geoTuple(geos), sep="\n")