import pandas
from geopy.distance import great_circle


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

    def __init__(self, anchor, times, totalNumPassengers, PickupAddress, DropoffAddress, PickupCoords, DropoffCoords):
        self.anchor = anchor
        self.times = times
        self.totalNumPassengers = totalNumPassengers
        self.PickupAddress = PickupAddress
        self.DropoffAddress = DropoffAddress
        self.pickupcoords = tuple(float(geo) for geo in PickupCoords.split(','))
        self.dropoffcoords = tuple(float(geo) for geo in DropoffCoords.split(','))

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
        valid = lambda x, y: 41 < x < 43.5 and -72.5 < y < - 70.5
        return valid(self.pickupcoords[0], self.pickupcoords[1]) and \
                valid(self.dropoffcoords[0], self.dropoffcoords[1])


class AllTrips:
    def __init__(self, infile):
        self.trips = []
        for i, trip in pandas.read_csv(infile).iterrows():
            geoTrip = Trip(trip['Anchor'], trip['RequestTime'], trip['Companions'] + 1, trip['PickFullAddress'],
                            trip['DropFullAddress'], trip['PickGeo'], trip['DropGeo'])
            if geoTrip.valid_trip():
                self.trips.append(geoTrip)
        self.locations = [pickup for trip in self.trips for pickup in [trip.pickupcoords, trip.dropoffcoords]]
        self.starttimes = [int(time) for trip in self.trips for time in [trip.earliestPickup, trip.earliestDropoff]]
        self.endtimes = [int(time) for trip in self.trips for time in [trip.latestPickup, trip.latestDropoff]]
        self.demands = [demand for _ in self.trips for demand in [1, -1]]

    def testIt(self):
        #print(self.locations, self.starttimes, self.endtimes, self.demands, sep='\n')
        for i in range(0, len(self.locations)):
            if self.starttimes[i] < 0:
                print(self.trips[int(i / 2)].PickupAddress)
                print(self.trips[int(i / 2)].dropoffcoords)
                print(self.starttimes[i])
                print(self.starttimes[i + 1])
                print(self.endtimes[i + 1])



s = AllTrips('MockData.csv')

s.testIt()