import pandas, os, json
from urllib import request as req

GOOGLEKEY = "AIzaSyBUKXXrG-9SK0l1DumDiz3PKYYZTSY0Vq8"

data = pandas.read_csv('../Data.csv')

data['PickFullAddress'] = data['PickHouseNumber'].astype(str) + " " + data['PickAddress1'] + ", " + data['Pickcity'] + \
                          ", " + data['pickzip'].astype(str)
data['DropFullAddress'] = data['DropHouseNumber'].astype(str) + " " + data['DropAddress1'] + ", " + data['Dropcity'] + \
                      ", " + data['DropZip'].astype(str)

def geo_req(address):
    return "https://maps.googleapis.com/maps/api/geocode/json?address=" + address.replace(" ", "+") + "&key=" + GOOGLEKEY


def geo_lookup(addresses, outfile):
    if os.path.exists(outfile):
        with open(outfile, 'r') as jf:
            data = json.load(jf)
    else:
        data = dict()
    for address in addresses:
        if address in data:
            continue
        try:
            geo_data = json.load(req.urlopen(geo_req(address)))
        except Exception as e:
            print(e, address)
            continue
        if len(geo_data['results']) == 0:
            print(address, ': Failure')
            continue
        print(address, ': Success')
        location = geo_data['results'][0]['geometry']['location']
        latlong = ','.join([str(location['lat']), str(location['lng'])])
        data[address] = latlong
    with open(outfile, 'w') as out:
        json.dump(data, out, indent=4)


pickups = json.load(open('PickUpGeo.json'))

dropoffs = json.load(open('DropOffGeo.json'))

print(len(data))
data = data[data['PickFullAddress'].isin(pickups)][data['DropFullAddress'].isin(dropoffs)]

data['PickGeo'] = data['PickFullAddress'].map(pickups)

data['DropGeo'] = data['DropFullAddress'].map(dropoffs)
data.to_csv(path_or_buf="MockData.csv", index=False)




"""

def geo_lookup2(addresses, outfile):
    if os.path.exists(outfile):
        with open(outfile, 'r') as jf:
            data = json.load(jf)
    else:
        data = dict()
    for address in addresses:
        if address in data:
            continue
        try:
            address_url = "https://geocoding.geo.census.gov/geocoder/locations/address?" + \
            address.replace(" ", "+") + "&benchmark=9&format=json"
            geo_data = json.load(req.urlopen(address_url))['result']
        except Exception as e:
            print(e, address)
            continue
        if len(geo_data['addressMatches']) == 0:
            print(address, ': Failure')
            continue
        print(address, ': Success')
        location = geo_data['addressMatches'][0]['coordinates']
        latlong = ','.join([str(location['x']), str(location['y'])])
        data[address] = latlong
    with open(outfile, 'w') as out:
        json.dump(data, out, indent=4)

geo_lookup2(data['GeoPickAddr'].head(), 'PickUpGeo2.json')

"""
