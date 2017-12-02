import unittest, os
from ..RoutingCalculator import location_tools as tools
from ..RoutingCalculator import parser


class GreatCircleDistance(unittest.TestCase):
    def test_GCD(self):
        geocodes = {}
        failure = set()

        test_tripA = parser.Trip("P", "1:00 PM", "1", "43", "Brattle St", "CAMBRIDGE", "2138",
                                 "29", "ST. SAUVEUR CT", "CAMBRIDGE", "2138", geocodes, failure)
        test_tripC = parser.Trip("P", "1:00 PM", "1", "43", "Brattle St", "CAMBRIDGE", "2138",
                                 "43", "Brattle St", "CAMBRIDGE", "2138", geocodes, failure)

        test_tripB = parser.Trip("A", "2:00 PM", "1", "43", "Brattle St", "CAMBRIDGE", "2138",
                                 "29", "ST. SAUVEUR CT", "CAMBRIDGE", "2138", geocodes, failure)

        self.assertEqual(abs(test_tripA.time_for_travel()), 232.68405651298997)
        self.assertEqual(abs(test_tripB.time_for_travel()), 232.68405651298997)
        self.assertEqual(abs(test_tripC.time_for_travel()), 0)


class ValidTrip(unittest.TestCase):
    def test_validTrip(self):
        geocodes = {}
        failure = set()
        test_tripA = parser.Trip("P", "1:00 PM", "1", "43", "Brattle St", "CAMBRIDGE", "2138",
                                 "29", "ST. SAUVEUR CT", "CAMBRIDGE", "2138", geocodes, failure)

        test_tripB = parser.Trip("A", "2:00 PM", "1", "43", "Brattle St", "CAMBRIDGE", "2138",
                                 "29", "ST. SAUVEUR CT", "CAMBRIDGE", "2138", geocodes, failure)

        # invalid trip with an invalid drop off in San Francisco, too far
        test_tripInvalidDropOff = parser.Trip("A", "2:00 PM", "1", "43", "Brattle St", "CAMBRIDGE", "2138",
                                              "1999", "16TH AVENUE", "SAN FRANCISCO", "94122", geocodes, failure)

        # invalid trip with an invalid pickup and invalid drop off both in San Francisco, too far
        test_tripInvalidPickup = parser.Trip("A", "2:00 PM", "1", "277", "CIRCLE SQUARE RD", "SAN FRANCISCO", "94155",
                                             "1999", "16TH AVENUE", "SAN FRANCISCO", "94122", geocodes, failure)

        test_tripA.pickupcoords = (42.3742077, -71.1214233)
        test_tripA.dropoffcoords = (42.3772638, -71.153024)
        test_tripB.pickupcoords = (42.3772638, -71.153024)
        test_tripB.dropoffcoords = (42.3772638, -71.153024)

        self.assertEqual(test_tripA.valid_trip(), True)
        self.assertEqual(test_tripB.valid_trip(), True)
        self.assertEqual(test_tripInvalidDropOff.valid_trip(), False)
        self.assertEqual(test_tripInvalidPickup.valid_trip(), False)


class Time_Windows(unittest.TestCase):
    def test_time_windows_pickup_arrival(self):
        geocodes = {}
        failure = set()

        tripa = parser.Trip("P", "1:00 PM", "1", "50", "ARSENAL ST", "WATERTOWN", "2472",
                            "468", "ARSENAL ST", "WATERTOWN", "2472", geocodes, failure)

        self.assertEqual(tripa.earliestDropoff, tools.time_to_seconds("1:00 PM") - 300 + tripa.time_for_travel())
        self.assertEqual(tripa.earliestPickup, tools.time_to_seconds("1:00 PM") - 300)
        self.assertEqual(tripa.latestDropoff, tools.time_to_seconds("1:00 PM") + 900 + tripa.time_for_travel())
        self.assertEqual(tripa.latestPickup, tools.time_to_seconds("1:00 PM") + 900)

        self.assertEqual(tripa.earliestDropoff, 46654.956821359854)
        self.assertEqual(tripa.earliestPickup, 46500)
        self.assertEqual(tripa.latestDropoff, 47854.956821359854)
        self.assertEqual(tripa.latestPickup, 47700)

        tripb = parser.Trip("A", "2:00 PM", "1", "50", "ARSENAL ST", "WATERTOWN", "2472",
                            "468", "ARSENAL ST", "WATERTOWN", "2472", geocodes, failure)

        self.assertEqual(tripb.earliestDropoff, tools.time_to_seconds("2:00 PM") - 1200)
        self.assertEqual(tripb.earliestPickup, tools.time_to_seconds("2:00 PM") - tripb.time_for_travel() - 1200)
        self.assertEqual(tripb.latestDropoff, tools.time_to_seconds("2:00 PM"))
        self.assertEqual(tripb.latestPickup, tools.time_to_seconds("2:00 PM") - tripb.time_for_travel())

        self.assertEqual(tripb.earliestDropoff, 49200)
        self.assertEqual(tripb.earliestPickup, 49045.043178640146)
        self.assertEqual(tripb.latestDropoff, 50400)
        self.assertEqual(tripb.latestPickup, 50245.043178640146)


# Tests for the Manhattan Distance
class Manhattan_Distance(unittest.TestCase):
    def test_manhatten_distance(self):
        pickup = [10, 10]
        dropoff = [15, 15]
        self.assertTrue(abs(tools.distance(pickup[0], pickup[1], dropoff[0], dropoff[1]) - 482) < 1)

    def test_manhatten_distance2(self):
        geocodes = {}
        failure = set()

        pickup = [10, 10]
        dropoff = [15, 15]
        self.assertTrue(abs(tools.distance(pickup[0], pickup[1], dropoff[0], dropoff[1]) - 482) < 1)

        tripb = parser.Trip("P", "1:00 PM", "1", "75", "Liverpool St", "EAST BOSTON", "2128",
                            "272", "BRANDYWYNE DR", "EAST BOSTON", "2128", geocodes, failure)

        tripb.pickupcoords = (42.3718638, -71.04096969999999)
        tripb.dropoffcoords = (42.3873459, -71.0134044)

        self.assertEqual(abs(tripb.time_for_travel()), 254.57535846730815)


# Test for parser.AllTrips Class
class All_Trips(unittest.TestCase):
    # test that the lengths of the locations, start times, and end times are all equal
    def test_lengths(self):
        input = [{"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 43,
                  "PickAddress1": "Brattle St",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2138,
                  "DropHouseNumber": 1184,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446},

                 {"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 28,
                  "PickAddress1": "WILSON WAY",
                  "Pickcity": "WESTWOOD",
                  "pickzip": 2090,
                  "DropHouseNumber": 27,
                  "DropAddress1": "WILSON WAY",
                  "Dropcity": "WESTWOOD",
                  "DropZip": 2090},

                 {"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 24,
                  "PickAddress1": "WALDEN SQUARE RD",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2140,
                  "DropHouseNumber": 415,
                  "DropAddress1": "MASSACHUSETTS AVE",
                  "Dropcity": "BOSTON",
                  "DropZip": 2118},

                 {"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 42,
                  "PickAddress1": "MAPLE AVE",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2139,
                  "DropHouseNumber": 235,
                  "DropAddress1": "HIGHLAND AVE",
                  "Dropcity": "SOMVERVILLE",
                  "DropZip": 2143,
                  }]

        trips1 = parser.AllTrips(input, tools.geo_path, tools.fail_path)
        self.assertEqual(9, len(trips1.locations))

        for i in range(0, len(trips1.locations)):
            pass
        self.assertEqual(len(trips1.starttimes), len(trips1.endtimes))
        self.assertEqual(len(trips1.starttimes), len(trips1.locations))
        self.assertEqual(len(trips1.locations), len(trips1.endtimes))
        self.assertEqual(len(trips1.locations), len(trips1.addresses))
        self.assertEqual(len(trips1.locations), len(trips1.demands))

    def test_parser_issues(self):
        input = [{"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 43,
                  "PickAddress1": "Brattle St",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2138,
                  "DropHouseNumber": 1184,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446}]
        trips1 = parser.AllTrips(input, "sample_file.json", "sample_file2.json")
        self.assertEqual(set(), trips1.fail_set)

    def test_one_bad_address_one_good(self):
        failure = set()
        success = {}
        trip1 = parser.Trip("P", "1:00 PM", "1", "43", "St", "CAMBRIDGE", "2138",
                            "29", "ST. SAUVEUR CT", "CAMBRIDGE", "2138", success, failure)

        self.assertEqual(1, len(success))
        self.assertEqual(1, len(failure))

    def tearDown(self):
        try:
            os.remove("sample_file.json")
            os.remove("sample_file2.json")
        except OSError as oserr:
            print(oserr)


# Tests for geo_lookup
class Geo_Lookup(unittest.TestCase):
    # test that when the pickup address is in the fail set, the pickup coords of the trip are 'None'
    def test_geo_lookup_failPickup(self):
        trip1 = parser.Trip("A", "6:00 PM", "1", "232", "SAINT PAUL ST", "BROOKLINE", "2445", "13", "Pierce St",
                            "BROOKLINE", "2445", {"149 SUTHERLAND RD BRIGHTON 2135": "42.34075,-71.1474"},
                            {'13 Pierce St BROOKLINE 2445', '149 SUTHERLAND RD BRIGHTON 2135'})
        self.assertEqual(None, trip1.pickupcoords)
        self.assertEqual(None, trip1.geo_lookup({"149 SUTHERLAND RD BRIGHTON 2135": "42.34075,-71.1474"},
                                                {'13 Pierce St BROOKLINE 2445', '149 SUTHERLAND RD BRIGHTON 2135'}))

    # test that when the pickup address is in the dict, the pickup coords are set accordingly
    def test_geo_lookup_successPickup(self):
        trip1 = parser.Trip("A", "6:00 PM", "1", "149", "SUTHERLAND RD", "BRIGHTON", "2135", "232", "SAINT PAUL ST",
                            "BROOKLINE", "2445", {"149 SUTHERLAND RD BRIGHTON 2135": "42.34075,-71.1474"},
                            {'13 Pierce St BROOKLINE 2445', '63 EVERETT ST ALLSTON 2134'})
        self.assertEqual((42.34075, -71.1474), trip1.pickupcoords)
        # self.assertEqual((42.34075,-71.1474), trip1.geo_lookup({"149 SUTHERLAND RD BRIGHTON 2135": "42.34075,-71.1474"},
        #                    {'13 Pierce St BROOKLINE 2445', '63 EVERETT ST ALLSTON 2134'}))

    # test that when the dropoff address is in the fail set, the dropoff coords of the trip are "None"
    def test_geo_lookup_failDropoff(self):
        trip1 = parser.Trip("P", "3:00 PM", "2", "232", "SAINT PAUL ST", "BROOKLINE", "2445", "13", "Pierce St",
                            "BROOKLINE", "2445", {"152 SUTHERLAND RD BRIGHTON 2135": "42.340794,-71.1474"},
                            {"13 Pierce St BROOKLINE 2445"})
        self.assertEqual(None, trip1.dropoffcoords)
        self.assertEqual(None, trip1.geo_lookup({"152 SUTHERLAND RD BRIGHTON 2135": "42.340794,-71.1474"},
                                                {"13 Pierce St BROOKLINE 2445"}))

    # test that when the dropoff address is in the dict, the dropoff coords are set accordingly
    def test_geo_lookup_successDropoff(self):
        trip1 = parser.Trip("P", "3:00 PM", "2", "232", "SAINT PAUL ST", "BROOKLINE", "2445", "149", "SUTHERLAND RD",
                            "BRIGHTON", "2135", {"149 SUTHERLAND RD BRIGHTON 2135": "42.34075,-71.1474"},
                            {"13 Pierce St BROOKLINE 2445"})
        self.assertEqual((42.34075, -71.1474), trip1.dropoffcoords)
        # self.assertEqual((42.34075,-71.1474), trip1.geo_lookup({"149 SUTHERLAND RD BRIGHTON 2135": "42.34075,-71.1474"},
        #                     {"13 Pierce St BROOKLINE 2445"}))


# Tests for lookup
class Lookup(unittest.TestCase):
    # lookup
    def test_lookup(self):
        trip1 = parser.Trip("P", "3:00 PM", "2", "232", "SAINT PAUL ST", "BROOKLINE", "2445", "149", "SUTHERLAND RD",
                            "BRIGHTON", "2135", {"149 SUTHERLAND RD BRIGHTON 2135": "42.34075,-71.1474"},
                            {"13 Pierce St BROOKLINE 2445"})
        self.assertEqual(None, trip1.lookup("SUTHERLAND RD", 149, "SUTHERLAND RD", "BRIGHTON", 42.34075, -71.1474,
                                            {"149 SUTHERLAND RD BRIGHTON 2135"}))


# To test the time to seconds and seconds to time converter
class TimeAndSecondsConverter(unittest.TestCase):
    def test_time__to_secondsconverter(self):
        time1 = "3:30 PM"
        time2 = "12:18 AM"
        time3 = "12:00 AM"
        time4 = "12:01 AM"
        time5 = "11:59 AM"
        time6 = "11:59 PM"
        time7 = "12:09 PM"
        time8 = "12:08 AM"
        time9 = "12:00 PM"

        self.assertEqual(tools.time_to_seconds(time1), 55800)
        self.assertEqual(tools.time_to_seconds(time2), 1080)
        self.assertEqual(tools.time_to_seconds(time3), 0)
        self.assertEqual(tools.time_to_seconds(time5), 43140)
        self.assertEqual(tools.time_to_seconds(time7), 43740)
        self.assertEqual(tools.time_to_seconds(time8), 480)
        self.assertEqual(tools.time_to_seconds(time6), 86340)
        self.assertEqual(tools.time_to_seconds(time4), 60)
        self.assertEqual(tools.time_to_seconds(time9), 43200)

    # To test that times from seconds get correctly converted into readable AM/PM time.
    def test_seconds_to_time_converter(self):
        time1 = 1130
        time2 = 55800
        time3 = 0
        time4 = 508
        time5 = 103
        time6 = 540
        time7 = 43140
        time8 = 86340
        time9 = 43200

        self.assertEqual(tools.seconds_to_time(time2), '3:30 PM')
        self.assertEqual(tools.seconds_to_time(time1), '12:18 AM')
        self.assertEqual(tools.seconds_to_time(time3), '12:00 AM')
        self.assertEqual(tools.seconds_to_time(time5), '12:01 AM')
        self.assertEqual(tools.seconds_to_time(time7), '11:59 AM')
        self.assertEqual(tools.seconds_to_time(time8), '11:59 PM')
        self.assertEqual(tools.seconds_to_time(time6), '12:09 AM')
        self.assertEqual(tools.seconds_to_time(time4), '12:08 AM')
        self.assertEqual(tools.seconds_to_time(time9), '12:00 PM')
