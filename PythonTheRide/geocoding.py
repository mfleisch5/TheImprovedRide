import pandas, os, json
from urllib import request as req

GOOGLEKEY = "AIzaSyBUKXXrG-9SK0l1DumDiz3PKYYZTSY0Vq8"
data = pandas.read_csv('../Data.csv')
data['PickFullAddress'] = data['PickHouseNumber'].astype(str) + " " + data['PickAddress1'] + ", " + data['Pickcity'] + \
                          ", " + data['pickzip'].astype(str)
data['DropFullAddress'] = data['DropHouseNumber'].astype(str) + " " + data['DropAddress1'] + " " + data['Dropcity'] + \
                      " " + data['DropZip'].astype(str)


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

geo_lookup(data['PickFullAddress'], 'PickUpGeo.json')