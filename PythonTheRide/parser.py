import pandas as pd, json, os
from geopy.distance import great_circle
from urllib import request as req


def time_to_seconds(time):
    array = time.split()
    time = array[0]
    pm = array[1] == 'PM'
    time = time.split(":")

    hour = int(time[0])
    minutes = int(time[1])

    if pm and hour != 12:
        hour = int(hour) + 12
    if hour == 12 and not pm:
        hour = 0

    return hour * 60 * 60 + minutes * 60


class Trip:
    """
    Create callback to calculate distances and travel times between points.
    """

    def __init__(self, anchor, times, passengers, p_num, p_street, p_city, p_zip, d_num, d_street, d_city,
                 d_zip, geo_dict, fail_set):
        self.anchor = anchor
        self.times = times
        self.passengers = passengers
        self.p_num = p_num
        self.p_street = p_street
        self.p_city = p_city
        self.p_zip = p_zip
        self.d_num = d_num
        self.d_street = d_street
        self.d_city = d_city
        self.d_zip = d_zip
        self.geo_lookup(geo_dict, fail_set)

        if self.pickupcoords is not None and self.dropoffcoords is not None:
            self.set_times()

    def set_times(self):
        """
        Sets the earliest and latest pickup and drop off times as long as coordinates are valid
        :return:
        """
        if self.anchor == "P":
            # specified pickup time, 5 minutes early.
            self.earliestPickup = time_to_seconds(str(self.times)) - 300
            # given pickup time, we are 15 minutes late.
            self.latestPickup = time_to_seconds(str(self.times)) + 900
            # We are given pickup time, caluclate  pickup time, and are 5 min early
            self.earliestDropoff = time_to_seconds(self.times) - 300 + self.time_for_travel()
            # we are given pickup time, add travel time, and are 20 minutes
            self.latestDropoff = time_to_seconds(self.times) + self.time_for_travel() + 900
        else:
            # this means the dropoff time is given. calculate the time it takes to drive, and then 5 minutes early
            self.earliestPickup = time_to_seconds(str(self.times)) - self.time_for_travel() - 300
            # given dropoff time, we calucate when to arrive, and then are 15 minutes late.
            self.latestPickup = time_to_seconds(str(self.times)) - self.time_for_travel() + 900
            # we are given dropoff time. It's earliest pickup time + travel time
            self.earliestDropoff = time_to_seconds(self.times) - 1200
            self.latestDropoff = time_to_seconds(self.times)

    def time_for_travel(self):
        return great_circle(self.pickupcoords, self.dropoffcoords).miles * 3600 / 25

    def valid_trip(self):
        if self.pickupcoords is None or self.dropoffcoords is None:
            return False
        valid = lambda x, y: 41 < x < 43.5 and -72.5 < y < - 70.5
        return valid(self.pickupcoords[0], self.pickupcoords[1]) and valid(self.dropoffcoords[0], self.dropoffcoords[1])

    def geo_lookup(self, geo_dict, fail_set):
        full_pick = " ".join([str(self.p_num), self.p_street, self.p_city, str(self.p_zip)])
        full_drop = " ".join([str(self.d_num), self.d_street, self.d_city, str(self.d_zip)])
        if full_pick in geo_dict:
            self.pickupcoords = tuple(float(geo) for geo in geo_dict[full_pick].split(','))
        elif full_pick in fail_set:
            self.pickupcoords = None
        else:
            self.pickupcoords = Trip.lookup(full_pick, self.p_num, self.p_street, self.p_city, self.p_zip, geo_dict,
                                            fail_set)
        if full_drop in geo_dict:
            self.dropoffcoords = tuple(float(geo) for geo in geo_dict[full_drop].split(','))
        elif full_drop in fail_set:
            self.dropoffcoords = None
        else:
            self.dropoffcoords = Trip.lookup(full_drop, self.d_num, self.d_street, self.d_city, self.d_zip, geo_dict,
                                             fail_set)

    @staticmethod
    def lookup(addr, num, street, city, code, geo_dict, failure_set):
        try:
            address_url = "https://geocoding.geo.census.gov/geocoder/locations/address?" + \
                          "street=" + str(num) + "+" + street.replace(" ", "+") + "&city=" + city + "&zip=" + \
                          str(code) + "&benchmark=9&format=json"
            geo_data = json.load(req.urlopen(address_url))['result']
        except Exception as e:
            print(e, addr)
            failure_set.add(addr)
            return None
        if len(geo_data['addressMatches']) == 0:
            print(addr, ': Failure')
            failure_set.add(addr)
            return None
        print(addr, ': Success')
        location = geo_data['addressMatches'][0]['coordinates']
        latlong = ','.join([str(location['y']), str(location['x'])])
        geo_dict[addr] = latlong
        return tuple(float(geo) for geo in latlong.split(','))


class AllTrips:
    def __init__(self, in_json, geo_file, fail_file):
        self.trips = []
        self.geo_file = geo_file
        self.fail_file = fail_file
        if os.path.exists(self.geo_file):
            with open(self.geo_file, 'r') as gf:
                self.geo_data = json.load(gf)
        else:
            self.geo_data = dict()
        if os.path.exists(self.fail_file):
            with open(self.fail_file, 'r') as ff:
                self.fail_set = set(json.load(ff))
        else:
            self.fail_set = set()
        for i, trip in pd.read_json(path_or_buf=in_json).dropna(subset=['PickHouseNumber', 'DropHouseNumber']).iterrows():
            geoTrip = Trip(trip['Anchor'], trip['RequestTime'], trip['Companions'] + 1, trip['PickHouseNumber'],
                           trip['PickAddress1'], trip['Pickcity'], trip['pickzip'], trip['DropHouseNumber'],
                           trip['DropAddress1'], trip['Dropcity'], trip['DropZip'], self.geo_data, self.fail_set)
            if geoTrip.valid_trip():
                self.trips.append(geoTrip)
        with open(self.geo_file, 'w') as gf:
            json.dump(self.geo_data, gf, indent=4)
        with open(self.fail_file, 'w') as ff:
            json.dump(list(self.fail_set), ff)
        self.locations = [pickup for trip in self.trips for pickup in [trip.pickupcoords, trip.dropoffcoords]]
        self.starttimes = [int(time) for trip in self.trips for time in [trip.earliestPickup, trip.earliestDropoff]]
        self.endtimes = [int(time) for trip in self.trips for time in [trip.latestPickup, trip.latestDropoff]]
        self.demands = [demand for _ in self.trips for demand in [1, -1]]

    def testIt(self):
        for i in range(0, len(self.locations)):
            pass
        print(len(self.locations), len(self.starttimes), len(self.endtimes), sep='\n')
