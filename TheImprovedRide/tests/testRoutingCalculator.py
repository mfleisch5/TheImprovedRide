import unittest
from ..RoutingCalculator import RoutingCalculator
from ..RoutingCalculator import location_tools as tools

class TestRouteCalculator(unittest.TestCase):
    def test_outstr(self):
        input = [{"Anchor": "A",
                  "RequestTime": "3:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 43,
                  "PickAddress1": "Brattle St",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2138,
                  "DropHouseNumber": 1184,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446,
                  }]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 1)
        self.assertEqual(str(routes), "Route 1: Depot -> ->  Pickup at 43 Brattle St CAMBRIDGE 2138, Load(0) " +
                         "Time(2:34 PM, 2:54 PM) ->  Dropoff at 1184 BEACON ST BROOK" +
                         "LINE 2446, Load(2) Time(2:40 PM, 3:00 PM) -> Depot")

        # Prints Invalid Routes
    def test_invalid_routes(self):
        input = [{"Anchor": "A",
                  "RequestTime": "10:00 AM",
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
                  "RequestTime": "1:45 PM",
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
                  "RequestTime": "4:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 24,
                  "PickAddress1": "WALDEN SQUARE RD",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2140,
                  "DropHouseNumber": 29,
                  "DropAddress1": "ST. SAUVEUR CT",
                  "Dropcity": "CAMBRIDGE",
                  "DropZip": 2138},

                 {"Anchor": "A",
                  "RequestTime": "2:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 42,
                  "PickAddress1": "MAPLE AVE",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2139,
                  "DropHouseNumber": 235,
                  "DropAddress1": "HIGHLAND AVE",
                  "Dropcity": "SOMERVILLE",
                  "DropZip": 2143,
                  }]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 9)
        self.assertRaises(Exception, routes)

        # to tests the route calculator with 4 trips in same towns

    def test_four_trips_same_town(self):
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
                  "DropHouseNumber": 29,
                  "DropAddress1": "ST. SAUVEUR CT",
                  "Dropcity": "CAMBRIDGE",
                  "DropZip": 2138},

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

        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 4)
        i = str(routes)
        self.maxDiff = None

        self.assertEqual(i,
                         "Route 1: Depot -> ->  Pickup at 43 Brattle St CAMBRIDGE 2138, Load(0) "
                         "Time(11:34 AM, 11:48 AM) ->  Pickup at 42 MAPLE AVE CAMBRIDGE 2139, Load(2) "
                         "Time(11:37 AM, 11:48 AM) ->  Dropoff at 235 HIGHLAND AVE SOMVERVILLE 2143, "
                         "Load(4) Time(11:40 AM, 11:50 AM) ->  Pickup at 24 WALDEN SQUARE RD CAMBRIDGE 2140, "
                         "Load(2) Time(11:42 AM, 11:52 AM) ->  Dropoff at 29 ST. SAUVEUR CT CAMBRIDGE 2138, Load(4) "
                         "Time(11:44 AM, 11:55 AM) ->  Dropoff at 1184 BEACON ST BROOKLINE 2446, Load(2) "
                         "Time(11:49 AM, 12:00 PM) -> Depot\n\nRoute 2: Depot -> ->  Pickup at 28 WILSON WAY WESTWOOD 2090, "
                         "Load(0) Time(11:39 AM, 11:59 AM) ->  Dropoff at 27 WILSON WAY WESTWOOD 2090, Load(2) "
                         "Time(11:40 AM, 12:00 PM) -> Depot")

        # Calculate a route where two pickups are from the same town (ridesharing 2 people). Pickup in succession, dropoff in succession

    def test_4trips_difftimes_sameRoute(self):
        input = [{"Anchor": "A",
                  "RequestTime": "10:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 339,
                  "PickAddress1": "MASSACHUSETTS AVE",
                  "Pickcity": "BOSTON",
                  "pickzip": 2115,
                  "DropHouseNumber": 1205,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446},

                 {"Anchor": "A",
                  "RequestTime": "1:00 PM",
                  "Companions": 2,
                  "PickHouseNumber": 12,
                  "PickAddress1": "ALCOTT LN",
                  "Pickcity": "WESTWOOD",
                  "pickzip": 2090,
                  "DropHouseNumber": 600,
                  "DropAddress1": "PLEASANT ST",
                  "Dropcity": "NORWOOD",
                  "DropZip": 2062},

                 {"Anchor": "A",
                  "RequestTime": "9:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 37,
                  "PickAddress1": "LAUREL ST",
                  "Pickcity": "SOMERVILLE",
                  "pickzip": 2143,
                  "DropHouseNumber": 104,
                  "DropAddress1": "CAMBRIDGESIDE PL",
                  "Dropcity": "CAMBRIDGE",
                  "DropZip": 2141},

                 {"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 0,
                  "PickHouseNumber": 42,
                  "PickAddress1": "MAPLE AVE",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2139,
                  "DropHouseNumber": 235,
                  "DropAddress1": "HIGHLAND AVE",
                  "Dropcity": "SOMVERVILLE",
                  "DropZip": 2143,
                  }]

        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 9)
        i = str(routes)
        self.maxDiff = None

        self.assertEqual(i,
                         "Route 1: Depot -> ->  Pickup at 37 LAUREL ST SOMERVILLE 2143, Load(0) Time(8:35 AM, 8:55 AM) ->  "
                         "Dropoff at 104 CAMBRIDGESIDE PL CAMBRIDGE 2141, Load(2) Time(8:40 AM, 9:00 AM) ->  "
                         "Pickup at 42 MAPLE AVE CAMBRIDGE 2139, Load(0) Time(11:37 AM, 11:57 AM) ->  "
                         "Dropoff at 235 HIGHLAND AVE SOMVERVILLE 2143, Load(1) Time(11:40 AM, 12:00 PM) ->  "
                         "Pickup at 12 ALCOTT LN WESTWOOD 2090, Load(0) Time(12:32 PM, 12:52 PM) ->  "
                         "Dropoff at 600 PLEASANT ST NORWOOD 2062, Load(3) Time(12:40 PM, 1:00 PM) ->  "
                         "Pickup at 339 MASSACHUSETTS AVE BOSTON 2115, Load(0) Time(9:36 PM, 9:56 PM) ->  "
                         "Dropoff at 1205 BEACON ST BROOKLINE 2446, Load(2) Time(9:40 PM, 10:00 PM) -> Depot")

    def test_10_stops(self):
        input = [{"Anchor": "A",
                  "RequestTime": "9:40 AM",
                  "Companions": 2,
                  "PickHouseNumber": 143,
                  "PickAddress1": "RIVERSIDE ST",
                  "Pickcity": "WATERTOWN",
                  "pickzip": 2472,
                  "DropHouseNumber": 3922,
                  "DropAddress1": "MYSTIC VALLEY PKWY",
                  "Dropcity": "MEDFORD",
                  "DropZip": 2155},

                 {"Anchor": "A",
                  "RequestTime": "3:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 12,
                  "PickAddress1": "ALCOTT LN",
                  "Pickcity": "WESTWOOD",
                  "pickzip": 2090,
                  "DropHouseNumber": 600,
                  "DropAddress1": "PLEASANT ST",
                  "Dropcity": "NORWOOD",
                  "DropZip": 2062},

                 {"Anchor": "A",
                  "RequestTime": "9:50 AM",
                  "Companions": 1,
                  "PickHouseNumber": 37,
                  "PickAddress1": "LAUREL ST",
                  "Pickcity": "SOMERVILLE",
                  "pickzip": 2143,
                  "DropHouseNumber": 104,
                  "DropAddress1": "CAMBRIDGESIDE PL",
                  "Dropcity": "CAMBRIDGE",
                  "DropZip": 2141},

                 {"Anchor": "A",
                  "RequestTime": "2:45 PM",
                  "Companions": 1,
                  "PickHouseNumber": 42,
                  "PickAddress1": "MAPLE AVE",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2139,
                  "DropHouseNumber": 235,
                  "DropAddress1": "HIGHLAND AVE",
                  "Dropcity": "SOMVERVILLE",
                  "DropZip": 2143,
                  },
                 {"Anchor": "A",
                  "RequestTime": "10:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 100,
                  "PickAddress1": "MASSACHUSETTS AVE",
                  "Pickcity": "BOSTON",
                  "pickzip": 2115,
                  "DropHouseNumber": 1,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446},
                 {"Anchor": "A",
                  "RequestTime": "7:30 AM",
                  "Companions": 1,
                  "PickHouseNumber": 265,
                  "PickAddress1": "Needham St",
                  "Pickcity": "NEWTON",
                  "pickzip": 2464,
                  "DropHouseNumber": 7005,
                  "DropAddress1": "GREAT MEADOW RD",
                  "Dropcity": "DEDHAM",
                  "DropZip": 2026},
                 {"Anchor": "A",
                  "RequestTime": "11:30 AM",
                  "Companions": 2,
                  "PickHouseNumber": 13,
                  "PickAddress1": "WOODCLIFF ST",
                  "Pickcity": "DORCHESTER",
                  "pickzip": 2125,
                  "DropHouseNumber": 262,
                  "DropAddress1": "TREMONT ST",
                  "Dropcity": "BOSTON",
                  "DropZip": 2116},
                 {"Anchor": "A",
                  "RequestTime": "8:30 PM",
                  "Companions": 2,
                  "PickHouseNumber": 317,
                  "PickAddress1": "WATER ST",
                  "Pickcity": "QUINCY",
                  "pickzip": 2169,
                  "DropHouseNumber": 74,
                  "DropAddress1": "CLEVELAND AVE",
                  "Dropcity": "BRAINTREE",
                  "DropZip": 2184},
                 {"Anchor": "A",
                  "RequestTime": "1:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 70,
                  "PickAddress1": "Bay View Dr",
                  "Pickcity": "SWAMPSCOTT",
                  "pickzip": 1907,
                  "DropHouseNumber": 345,
                  "DropAddress1": "SQUIRE RD",
                  "Dropcity": "REVERE",
                  "DropZip": 2151},
                 {"Anchor": "A",
                  "RequestTime": "4:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 521,
                  "PickAddress1": "SHERMAN ST",
                  "Pickcity": "CANTON",
                  "pickzip": 2115,
                  "DropHouseNumber": 1158,
                  "DropAddress1": "CENTRE ST",
                  "Dropcity": "JAMAICA PLAIN",
                  "DropZip": 2130}]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 21)
        i = str(routes)
        self.maxDiff = None
        self.assertEqual(i,
                         "Route 1: Depot -> ->  Pickup at 12 ALCOTT LN WESTWOOD 2090, Load(0) Time(2:32 PM, 2:52 PM) ->  "
                         "Dropoff at 600 PLEASANT ST NORWOOD 2062, Load(2) Time(2:40 PM, 3:00 PM) -> Depot\n\n"
                         "Route 2: Depot -> ->  Pickup at 37 LAUREL ST SOMERVILLE 2143, Load(0) Time(9:25 AM, 9:45 AM) ->  "
                         "Dropoff at 104 CAMBRIDGESIDE PL CAMBRIDGE 2141, Load(2) Time(9:30 AM, 9:50 AM) ->  "
                         "Pickup at 13 WOODCLIFF ST DORCHESTER 2125, Load(0) Time(11:04 AM, 11:24 AM) ->  "
                         "Dropoff at 262 TREMONT ST BOSTON 2116, Load(3) Time(11:10 AM, 11:30 AM) ->  "
                         "Pickup at 70 Bay View Dr SWAMPSCOTT 1907, Load(0) Time(12:25 PM, 12:45 PM) ->  "
                         "Dropoff at 345 SQUIRE RD REVERE 2151, Load(2) Time(12:40 PM, 1:00 PM) ->  "
                         "Pickup at 42 MAPLE AVE CAMBRIDGE 2139, Load(0) Time(2:22 PM, 2:42 PM) ->  "
                         "Dropoff at 235 HIGHLAND AVE SOMVERVILLE 2143, Load(2) Time(2:25 PM, 2:45 PM) ->  "
                         "Pickup at 317 WATER ST QUINCY 2169, Load(0) Time(8:05 PM, 8:25 PM) ->  "
                         "Dropoff at 74 CLEVELAND AVE BRAINTREE 2184, Load(3) Time(8:10 PM, 8:30 PM) -> Depot")

    # Tests 5 stops invalid
    def test_5stops_invalid2(self):
        # Initialize Stops
        id = 1
        id2 = 2
        id3 = 3
        id4 = 4
        id5 = 5
        addr = "12 ALCOTT LN, WESTWOOD, 2090"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("3:00 PM"),
                       tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        stop2 = RoutingCalculator.Stop(id2, addr, dropoff, time_window, curr_load)

        stop3 = RoutingCalculator.Stop(id3, addr, dropoff, time_window, curr_load)
        stop4 = RoutingCalculator.Stop(id4, addr, dropoff, time_window, curr_load)
        stop5 = RoutingCalculator.Stop(id5, addr, dropoff, time_window, curr_load)

        # Initialize a Route
        route1 = RoutingCalculator.Route()
        # Add 5 stops
        route1.add_stop(stop1)
        route1.add_stop(stop2)
        route1.add_stop(stop3)
        route1.add_stop(stop4)
        route1.add_stop(stop5)

        self.maxDiff = None
        self.assertEqual(route1.valid(), False)

    # Tests 5 stops won't output anything
    def test_5stops_invalid(self):
        input = [{"Anchor": "A",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 339,
                  "PickAddress1": "MASSACHUSETTS AVE",
                  "Pickcity": "BOSTON",
                  "pickzip": 2115,
                  "DropHouseNumber": 1205,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446},

                 {"Anchor": "A",
                  "RequestTime": "11:00 AM",
                  "Companions": 2,
                  "PickHouseNumber": 12,
                  "PickAddress1": "ALCOTT LN",
                  "Pickcity": "WESTWOOD",
                  "pickzip": 2090,
                  "DropHouseNumber": 600,
                  "DropAddress1": "PLEASANT ST",
                  "Dropcity": "NORWOOD",
                  "DropZip": 2062},

                 {"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 0,
                  "PickHouseNumber": 42,
                  "PickAddress1": "MAPLE AVE",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2139}]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 6)
        i = str(routes)
        self.assertEqual(i, "")

    # Tests example 20 trips
    def test_20trips(self):
        input = [{"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 2,
                  "PickHouseNumber": 143,
                  "PickAddress1": "RIVERSIDE ST",
                  "Pickcity": "WATERTOWN",
                  "pickzip": 2472,
                  "DropHouseNumber": 3922,
                  "DropAddress1": "MYSTIC VALLEY PKWY",
                  "Dropcity": "MEDFORD",
                  "DropZip": 2155},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 12,
                  "PickAddress1": "ALCOTT LN",
                  "Pickcity": "WESTWOOD",
                  "pickzip": 2090,
                  "DropHouseNumber": 600,
                  "DropAddress1": "PLEASANT ST",
                  "Dropcity": "NORWOOD",
                  "DropZip": 2062},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 37,
                  "PickAddress1": "LAUREL ST",
                  "Pickcity": "SOMERVILLE",
                  "pickzip": 2143,
                  "DropHouseNumber": 104,
                  "DropAddress1": "CAMBRIDGESIDE PL",
                  "Dropcity": "CAMBRIDGE",
                  "DropZip": 2141},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 42,
                  "PickAddress1": "MAPLE AVE",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2139,
                  "DropHouseNumber": 235,
                  "DropAddress1": "HIGHLAND AVE",
                  "Dropcity": "SOMERVILLE",
                  "DropZip": 2143,
                  },
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 100,
                  "PickAddress1": "MASSACHUSETTS AVE",
                  "Pickcity": "BOSTON",
                  "pickzip": 2115,
                  "DropHouseNumber": 1,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446},
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 265,
                  "PickAddress1": "Needham St",
                  "Pickcity": "NEWTON",
                  "pickzip": 2464,
                  "DropHouseNumber": 7005,
                  "DropAddress1": "GREAT MEADOW RD",
                  "Dropcity": "DEDHAM",
                  "DropZip": 2026},
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 2,
                  "PickHouseNumber": 13,
                  "PickAddress1": "WOODCLIFF ST",
                  "Pickcity": "DORCHESTER",
                  "pickzip": 2125,
                  "DropHouseNumber": 262,
                  "DropAddress1": "TREMONT ST",
                  "Dropcity": "BOSTON",
                  "DropZip": 2116},
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 2,
                  "PickHouseNumber": 317,
                  "PickAddress1": "WATER ST",
                  "Pickcity": "QUINCY",
                  "pickzip": 2169,
                  "DropHouseNumber": 74,
                  "DropAddress1": "CLEVELAND AVE",
                  "Dropcity": "BRAINTREE",
                  "DropZip": 2184},
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 70,
                  "PickAddress1": "Bay View Dr",
                  "Pickcity": "SWAMPSCOTT",
                  "pickzip": 1907,
                  "DropHouseNumber": 345,
                  "DropAddress1": "SQUIRE RD",
                  "Dropcity": "REVERE",
                  "DropZip": 2151},
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 521,
                  "PickAddress1": "SHERMAN ST",
                  "Pickcity": "CANTON",
                  "pickzip": 2115,
                  "DropHouseNumber": 1158,
                  "DropAddress1": "CENTRE ST",
                  "Dropcity": "JAMAICA PLAIN",
                  "DropZip": 2130},
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 18,
                  "PickAddress1": "WARREN AVE",
                  "Pickcity": "WOBURN",
                  "pickzip": 1801,
                  "DropHouseNumber": 8,
                  "DropAddress1": "OAKLAND ST",
                  "Dropcity": "LEXINGTON",
                  "DropZip": 2420},
                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 122,
                  "PickAddress1": "MOUNTAIN AVE",
                  "Pickcity": "MALDEN",
                  "pickzip": 2148,
                  "DropHouseNumber": 105,
                  "DropAddress1": "GARLAND ST",
                  "Dropcity": "EVERETT",
                  "DropZip": 2149},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 19,
                  "PickAddress1": "LAKEVIEW AVE",
                  "Pickcity": "READING",
                  "pickzip": 1867,
                  "DropHouseNumber": 16,
                  "DropAddress1": "GOVE ST",
                  "Dropcity": "EAST BOSTON",
                  "DropZip": 2128},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 138,
                  "PickAddress1": "BRIDGE ST",
                  "Pickcity": "BEVERLY",
                  "pickzip": 1915,
                  "DropHouseNumber": 101,
                  "DropAddress1": "INDEPENDENCE WAY",
                  "Dropcity": "DANVERS",
                  "DropZip": 1923},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 33,
                  "PickAddress1": "JAMES ST",
                  "Pickcity": "WINCHESTER",
                  "pickzip": 1890,
                  "DropHouseNumber": 1437,
                  "DropAddress1": "MAIN ST",
                  "Dropcity": "WALTHAM",
                  "DropZip": 2451},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 59,
                  "PickAddress1": "WETHERELL ST",
                  "Pickcity": "NEWTON UPPER FALLS",
                  "pickzip": 2464,
                  "DropHouseNumber": 30,
                  "DropAddress1": "DENBY RD",
                  "Dropcity": "ALLSTON",
                  "DropZip": 2134},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 10,
                  "PickAddress1": "CORCORAN RD",
                  "Pickcity": "BURLINGTON",
                  "pickzip": 1803,
                  "DropHouseNumber": 1437,
                  "DropAddress1": "MAIN ST",
                  "Dropcity": "WALTHAM",
                  "DropZip": 2451},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 14,
                  "PickAddress1": "WALNUT ST",
                  "Pickcity": "PEABODY",
                  "pickzip": 1960,
                  "DropHouseNumber": 156,
                  "DropAddress1": "S HUNTINGTON AVE",
                  "Dropcity": "JAMAICA PLAIN",
                  "DropZip": 2130},

                 {"Anchor": "P",
                  "RequestTime": "10:00 AM",
                  "Companions": 1,
                  "PickHouseNumber": 91,
                  "PickAddress1": "JASPER LN",
                  "Pickcity": "RANDOLPH",
                  "pickzip": 2368,
                  "DropHouseNumber": 6,
                  "DropAddress1": "FRUIT ST",
                  "Dropcity": "BOSTON",
                  "DropZip": 2114}]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 39)
        i = str(routes)
        self.maxDiff = None

        self.assertEqual(i,
                         "Route 1: Depot -> ->  Pickup at 14 WALNUT ST PEABODY 1960, Load(0) Time(9:55 AM, 9:55 AM) ->  Pickup at 138 BRIDGE ST BEVERLY 1915, Load(2) Time(9:59 AM, 10:00 AM) ->  Dropoff at 101 INDEPENDENCE WAY DANVERS 1923, Load(4) Time(10:02 AM, 10:03 AM) ->  Pickup at 70 Bay View Dr SWAMPSCOTT 1907, Load(2) Time(10:14 AM, 10:15 AM) ->  Dropoff at 345 SQUIRE RD REVERE 2151, Load(4) Time(10:28 AM, 10:29 AM) ->  Dropoff at 156 S HUNTINGTON AVE JAMAICA PLAIN 2130, Load(2) Time(10:47 AM, 10:55 AM) -> Depot\n\n"
                         "Route 2: Depot -> ->  Pickup at 18 WARREN AVE WOBURN 1801, Load(0) Time(9:55 AM, 10:05 AM) ->  Pickup at 10 CORCORAN RD BURLINGTON 1803, Load(2) Time(10:04 AM, 10:15 AM) ->  Dropoff at 8 OAKLAND ST LEXINGTON 2420, Load(4) Time(10:14 AM, 10:24 AM) ->  Dropoff at 1437 MAIN ST WALTHAM 2451, Load(2) Time(10:26 AM, 10:37 AM) -> Depot\n\n"
                         "Route 3: Depot -> ->  Pickup at 19 LAKEVIEW AVE READING 1867, Load(0) Time(9:55 AM, 10:00 AM) ->  Pickup at 122 MOUNTAIN AVE MALDEN 2148, Load(2) Time(10:09 AM, 10:15 AM) ->  Dropoff at 105 GARLAND ST EVERETT 2149, Load(4) Time(10:14 AM, 10:20 AM) ->  Dropoff at 16 GOVE ST EAST BOSTON 2128, Load(2) Time(10:20 AM, 10:40 AM) -> Depot\n\n"
                         "Route 4: Depot -> ->  Pickup at 59 WETHERELL ST NEWTON UPPER FALLS 2464, Load(0) Time(9:55 AM, 10:15 AM) ->  Dropoff at 30 DENBY RD ALLSTON 2134, Load(2) Time(10:07 AM, 10:27 AM) -> Depot\n\n"
                         "Route 5: Depot -> ->  Pickup at 13 WOODCLIFF ST DORCHESTER 2125, Load(0) Time(9:55 AM, 10:03 AM) ->  Pickup at 42 MAPLE AVE CAMBRIDGE 2139, Load(3) Time(10:04 AM, 10:12 AM) ->  Dropoff at 235 HIGHLAND AVE SOMERVILLE 2143, Load(5) Time(10:07 AM, 10:15 AM) ->  Pickup at 37 LAUREL ST SOMERVILLE 2143, Load(3) Time(10:07 AM, 10:15 AM) ->  Dropoff at 104 CAMBRIDGESIDE PL CAMBRIDGE 2141, Load(5) Time(10:09 AM, 10:18 AM) ->  Dropoff at 262 TREMONT ST BOSTON 2116, Load(3) Time(10:11 AM, 10:20 AM) -> Depot\n\n"
                         "Route 6: Depot -> ->  Pickup at 12 ALCOTT LN WESTWOOD 2090, Load(0) Time(9:55 AM, 10:15 AM) ->  Dropoff at 600 PLEASANT ST NORWOOD 2062, Load(2) Time(10:02 AM, 10:22 AM) -> Depot\n\n"
                         "Route 7: Depot -> ->  Pickup at 91 JASPER LN RANDOLPH 2368, Load(0) Time(9:55 AM, 10:03 AM) ->  Pickup at 317 WATER ST QUINCY 2169, Load(2) Time(10:07 AM, 10:15 AM) ->  Dropoff at 74 CLEVELAND AVE BRAINTREE 2184, Load(5) Time(10:09 AM, 10:19 AM) ->  Dropoff at 6 FRUIT ST BOSTON 2114, Load(2) Time(10:33 AM, 10:46 AM) -> Depot")

    def test_two_trips_same_town_pickup_pickup_dropoff_dropoff(self):
        input = [{"Anchor": "A",
                  "RequestTime": "3:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 24,
                  "PickAddress1": "DEVENS ST",
                  "Pickcity": "CHARLESTOWN",
                  "pickzip": 2129,
                  "DropHouseNumber": 75,
                  "DropAddress1": "LIVERPOOL St",
                  "Dropcity": "EAST BOSTON",
                  "DropZip": 2128
                  },
                 {"Anchor": "A",
                  "RequestTime": "3:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 388,
                  "PickAddress1": "MAIN ST",
                  "Pickcity": "CHARLESTOWN",
                  "pickzip": 2129,
                  "DropHouseNumber": 78,
                  "DropAddress1": "LIVERPOOL ST",
                  "Dropcity": "EAST BOSTON",
                  "DropZip": 2128}
                 ]

        self.maxDiff = None
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 2)
        self.assertEqual(str(routes), "Route 1: Depot -> ->  Pickup at 388 MAIN ST CHARLESTOWN 2129, Load(0) "
                                      "Time(2:36 PM, 2:56 PM) ->  Pickup at 24 DEVENS ST CHARLESTOWN 2129, "
                                      "Load(2) Time(2:37 PM, 2:57 PM) ->  Dropoff at 75 LIVERPOOL St EAST BOSTON 2128, "
                                      "Load(4) Time(2:40 PM, 3:00 PM) ->  Dropoff at 78 LIVERPOOL ST EAST BOSTON 2128, "
                                      "Load(2) Time(2:40 PM, 3:00 PM) -> Depot")

        # to test the route calculator with 2 trips in same towns different times

    def test_two_trips_same_town_diff_time(self):
        input = [{"Anchor": "A",
                  "RequestTime": "12:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 63,
                  "PickAddress1": "EVERETT ST",
                  "Pickcity": "ALLSTON",
                  "pickzip": 2134,
                  "DropHouseNumber": 152,
                  "DropAddress1": "SUTHERLAND RD",
                  "Dropcity": "BRIGHTON",
                  "DropZip": 2135},

                 {"Anchor": "A",
                  "RequestTime": "2:20 PM",
                  "Companions": 1,
                  "PickHouseNumber": 10,
                  "PickAddress1": "CORINNE RD",
                  "Pickcity": "BRIGHTON",
                  "pickzip": 2135,
                  "DropHouseNumber": 3,
                  "DropAddress1": "City Sq",
                  "Dropcity": "CHARLESTOWN",
                  "DropZip": 2129}]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 2)
        i = str(routes)
        self.maxDiff = None

        # should be pickup 1 dropoff 1 pickup 2 dropoff 2
        self.assertEqual(i, "Route 1: Depot -> ->  Pickup at 63 EVERETT ST ALLSTON 2134, " +
                         "Load(0) Time(11:37 AM, 11:57 AM) ->  Dropoff at 152 SUTHERLAND RD BRIGHTON 2135, " +
                         "Load(2) Time(11:40 AM, 12:00 PM) ->  Pickup at 10 CORINNE RD BRIGHTON 2135, " +
                         "Load(0) Time(1:47 PM, 2:07 PM) ->  Dropoff at 3 City Sq CHARLESTOWN 2129, " +
                         "Load(2) Time(2:00 PM, 2:20 PM) -> Depot")

    # to test the routing calculator with 4 trips at the same time in different towns

    def test_four_trips_same_time_diff_towns(self):
        input = [{"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 2,
                  "PickHouseNumber": 226,
                  "PickAddress1": "RUGGLES ST",
                  "Pickcity": "ROXBURY",
                  "pickzip": 2120,
                  "DropHouseNumber": 334,
                  "DropAddress1": "Plymouth St",
                  "Dropcity": "HOLBROOK",
                  "DropZip": 2343},

                 {"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 39,
                  "PickAddress1": "FRUIT ST",
                  "Pickcity": "BOSTON",
                  "pickzip": 2114,
                  "DropHouseNumber": 54,
                  "DropAddress1": "WILSON AVE",
                  "Dropcity": "QUINCY",
                  "DropZip": 2170},

                 {"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 2,
                  "PickHouseNumber": 106,
                  "PickAddress1": "FALLS BLVD",
                  "Pickcity": "QUINCY",
                  "pickzip": 2169,
                  "DropHouseNumber": 69,
                  "DropAddress1": "THOMPSON RD",
                  "Dropcity": "NORTH WEYMOUTH",
                  "DropZip": 219},

                 {"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 235,
                  "PickAddress1": "MIDDLE ST",
                  "Pickcity": "BRAINTREE",
                  "pickzip": 2184,
                  "DropHouseNumber": 3,
                  "DropAddress1": "HORAN WAY",
                  "Dropcity": "JAMAICA PLAIN",
                  "DropZip": 2130,
                  }]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 9)
        i = str(routes)
        self.maxDiff = None

        self.assertEqual(str(routes), "Route 1: Depot -> ->  Pickup at 39 FRUIT ST BOSTON 2114, "
                                      "Load(0) Time(3:55 PM, 4:15 PM) ->  Dropoff at 54 WILSON AVE QUINCY 2170, "
                                      "Load(2) Time(4:11 PM, 4:31 PM) -> Depot\n\nRoute 2: Depot -> ->  "
                                      "Pickup at 235 MIDDLE ST BRAINTREE 2184, Load(0) Time(3:55 PM, 4:15 PM) ->  "
                                      "Dropoff at 3 HORAN WAY JAMAICA PLAIN 2130, Load(2) Time(4:17 PM, 4:37 PM) -> Depot")
        # to test the routing calculator with 4 trips at the same time in different towns

    def test_four_trips_same_time_diff_towns2(self):
        input = [{"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 2,
                  "PickHouseNumber": 226,
                  "PickAddress1": "RUGGLES ST",
                  "Pickcity": "ROXBURY",
                  "pickzip": 2120,
                  "DropHouseNumber": 334,
                  "DropAddress1": "Plymouth St",
                  "Dropcity": "HOLBROOK",
                  "DropZip": 2343},

                 {"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 39,
                  "PickAddress1": "FRUIT ST",
                  "Pickcity": "BOSTON",
                  "pickzip": 2114,
                  "DropHouseNumber": 54,
                  "DropAddress1": "WILSON AVE",
                  "Dropcity": "QUINCY",
                  "DropZip": 2170},

                 {"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 2,
                  "PickHouseNumber": 106,
                  "PickAddress1": "FALLS BLVD",
                  "Pickcity": "QUINCY",
                  "pickzip": 2169,
                  "DropHouseNumber": 69,
                  "DropAddress1": "THOMPSON RD",
                  "Dropcity": "NORTH WEYMOUTH",
                  "DropZip": 219},

                 {"Anchor": "P",
                  "RequestTime": "4:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 235,
                  "PickAddress1": "MIDDLE ST",
                  "Pickcity": "BRAINTREE",
                  "pickzip": 2184,
                  "DropHouseNumber": 3,
                  "DropAddress1": "HORAN WAY",
                  "Dropcity": "JAMAICA PLAIN",
                  "DropZip": 2130,
                  }]
        routes = RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 4)
        i = str(routes)
        self.maxDiff = None

        self.assertEqual(str(routes), "Route 1: Depot -> ->  Pickup at 39 FRUIT ST BOSTON 2114, "
                                      "Load(0) Time(3:55 PM, 4:15 PM) ->  Dropoff at 54 WILSON AVE QUINCY 2170, "
                                      "Load(2) Time(4:11 PM, 4:31 PM) -> Depot\n\nRoute 2: Depot -> ->  "
                                      "Pickup at 235 MIDDLE ST BRAINTREE 2184, Load(0) Time(3:55 PM, 4:15 PM) ->  "
                                      "Dropoff at 3 HORAN WAY JAMAICA PLAIN 2130, Load(2) Time(4:17 PM, 4:37 PM) -> Depot")

    def test_num_locations_zero(self):
        input = [{"Anchor": "A",
                  "RequestTime": "3:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 43,
                  "PickAddress1": "Brattle St",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2138,
                  "DropHouseNumber": 1184,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446,
                  }]
        self.assertRaises(Exception, RoutingCalculator.main(input, tools.geo_path, tools.fail_path, 0))


# Tests for the Route class in the RoutingCalculator class
class TestRouteClassInRouteCalc(unittest.TestCase):
    # Tests for the add stop method in the route class
    def test_add_stop(self):
        # Initialize a Route
        route1 = RoutingCalculator.Route()
        # Initialize Stops
        id = 1
        id2 = 2
        id3 = 3
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("3:00 PM"),
                       tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        stop2 = RoutingCalculator.Stop(id2, addr, dropoff, time_window, curr_load)

        # Add stop1 to route 1
        route1.add_stop(stop1)

        self.assertTrue(route1.stops, 1)
        # See that Stop 1 is the first stop in route1's stop list
        self.assertEquals(route1.stops[0], stop1)
        # See that Stop 2 is not the first stop in route1's stop list
        self.assertNotEqual(route1.stops[0], stop2)

        # Now add stop2 to route1
        route1.add_stop(stop2)
        # See that stop2 is the second stop in route1's stop list
        self.assertEqual(route1.stops[1], stop2)
        # See that stop1 is still the first stop in route1's stop list
        self.assertEquals(route1.stops[0], stop1)
        # See that stop2 is not the first stop in route1's stop list
        self.assertNotEqual(route1.stops[0], stop2)

    # Test the string method in Route class
    def test_str(self):
        # Initialize a Route
        route1 = RoutingCalculator.Route()
        # Initialize Stops
        id = 1
        id2 = 2
        id3 = 3
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("3:00 PM"),
                       tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        # Add stop1 to route 1
        route1.add_stop(stop1)

        self.assertEqual(route1.__str__(), "Depot -> ->  Pickup at 95 TREMONT ST, " +
                         "BOSTON, 2108, Load(0) Time(3:00 PM, 3:15 PM) -> Depot")

    # Test for equality
    def test_eq(self):
        # Initialize Stops
        id = 1
        id2 = 2
        id3 = 3
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("3:00 PM"),
                       tools.time_to_seconds("3:15 PM"))
        curr_load = 0
        route1 = RoutingCalculator.Route()
        route1copy = RoutingCalculator.Route()
        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        route1.add_stop(stop1)
        route1copy.add_stop(stop1)

        self.assertEqual(route1, route1copy)

    # Tests for the valid method in the Route class
    def test_valid(self):
        # Initialize Stops
        id = 1
        id2 = 2
        id3 = 3
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("3:00 PM"),
                       tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        stop2 = RoutingCalculator.Stop(id2, addr, dropoff, time_window, curr_load)

        stop3 = RoutingCalculator.Stop(id3, addr, dropoff, time_window, curr_load)

        # Initialize a Route
        route1 = RoutingCalculator.Route()
        # Add two stops
        route1.add_stop(stop1)
        route1.add_stop(stop2)

        # Test that Route1 is valid
        self.assertEqual(route1.valid(), True)

        # Initialize a second Route
        route2 = RoutingCalculator.Route()

        # Add 3 stops, invalid route
        route2.add_stop(stop1)
        route2.add_stop(stop2)
        route2.add_stop(stop3)

        # Test that Route2 is invalid
        self.assertEqual(route2.valid(), False)


class TestStopClass(unittest.TestCase):
    # To test the Stop class, and ensure that an object is initialized correctly
    def test_stop_initializer(self):
        id = 1
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        time_window = (tools.time_to_seconds("3:00 PM"), tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stopa = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        self.assertEquals(1, stopa.id)
        self.assertEquals("95 TREMONT ST, BOSTON, 2108", stopa.addr)
        self.assertEquals(True, stopa.pickup)
        self.assertEqual((tools.time_to_seconds("3:00 PM"), tools.time_to_seconds("3:15 PM")), stopa.time_window)
        self.assertEqual(0, stopa.curr_load)
        self.assertEqual("95 TREMONT ST, BOSTON, 2108", stopa.to_dict()["Address"])
        self.assertEqual("Pickup", stopa.to_dict()["Type"])
        self.assertEqual(0, stopa.to_dict()["Load"])
        self.assertEqual("3:00 PM", stopa.to_dict()["Earliest"])
        self.assertEqual("3:15 PM", stopa.to_dict()["Latest"])

        id2 = 2
        addr2 = "95 TREMONT ST, BOSTON, 2108"
        pickup2 = False
        time_window2 = (tools.time_to_seconds("3:00 PM"), tools.time_to_seconds("3:15 PM"))
        curr_load2 = 0

        stopb = RoutingCalculator.Stop(id2, addr2, pickup2, time_window2, curr_load2)

        self.assertEquals(2, stopb.id)
        self.assertEquals("95 TREMONT ST, BOSTON, 2108", stopb.addr)
        self.assertEquals(False, stopb.pickup)
        self.assertEqual((tools.time_to_seconds("3:00 PM"), tools.time_to_seconds("3:15 PM")), stopb.time_window)
        self.assertEqual(0, stopb.curr_load)
        self.assertEqual("Dropoff", stopb.to_dict()["Type"])

    # To test that a stop object is converted to string correctly
    def test_stop_to_string(self):
        id = 1
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        time_window = (tools.time_to_seconds("3:00 PM"), tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stopa = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        self.assertEquals(" Pickup at 95 TREMONT ST, BOSTON, 2108, Load(0) Time(3:00 PM, 3:15 PM)", str(stopa))

        id = 2
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = False
        time_window = (tools.time_to_seconds("3:00 PM"), tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stopb = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        self.assertEquals(" Dropoff at 95 TREMONT ST, BOSTON, 2108, Load(0) Time(3:00 PM, 3:15 PM)", str(stopb))

    # To verify the equals method for a stop object
    def test_stop_equals(self):
        id = 1
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        time_window = (tools.time_to_seconds("3:00 PM"), tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stopa = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        self.assertEquals(" Pickup at 95 TREMONT ST, BOSTON, 2108, Load(0) Time(3:00 PM, 3:15 PM)", str(stopa))

        stopb = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        self.assertEqual(stopa, stopb)
        self.assertEqual(stopa, stopa)
        self.assertEqual(stopb, stopb)


class TestRouteCalcClass(unittest.TestCase):
    # test the add route method in the Routing Calculator class
    def test_add_route(self):
        # initialize routing calculator and 2 routes
        routingcalculator1 = RoutingCalculator.RoutingCalculator()
        route1 = RoutingCalculator.Route()
        route2 = RoutingCalculator.Route()

        # initialize stops
        id = 1
        id2 = 2
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("3:00 PM"),
                       tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        stop2 = RoutingCalculator.Stop(id2, addr, dropoff, time_window, curr_load)

        # Add stop1 to route 1
        route1.add_stop(stop1)

        # add route to routing calculator
        routingcalculator1.add_route(route1)

        # verify there is 1 route in routing calculator 1
        self.assertTrue(routingcalculator1.routes, 1)

        # add stop2 to route 2
        route2.add_stop(stop2)

        # add route2 to routing calculator
        routingcalculator1.add_route(route2)

        # verify route1 is the first route in routing calculator and not route2
        self.assertEqual(routingcalculator1.routes[0], route1)
        self.assertNotEquals(routingcalculator1.routes[0], route2)

    # test that a routing calculator with 1 route is valid
    def test_valid_routing_calculator1(self):
        # initialize routing calculator and route
        routingcalculator1 = RoutingCalculator.RoutingCalculator()
        route1 = RoutingCalculator.Route()

        # initialize stops
        id = 1
        id2 = 2
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("3:00 PM"),
                       tools.time_to_seconds("3:15 PM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        stop2 = RoutingCalculator.Stop(id2, addr, dropoff, time_window, curr_load)

        # Add stops to route 1
        route1.add_stop(stop1)
        route1.add_stop(stop2)

        # add route to routing calculator
        routingcalculator1.add_route(route1)

        # verify the routing calculator is valid
        self.assertTrue(True, routingcalculator1.valid())

    # test that a routing calculator with more than one route is valid
    def test_valid_routing_calculator2(self):
        # initialize routing calculator and 2 routes
        routingcalculator1 = RoutingCalculator.RoutingCalculator()
        route1 = RoutingCalculator.Route()
        route2 = RoutingCalculator.Route()

        # initialize stops
        id = 1
        id2 = 2
        addr = "63 EVERETT ST ALLSTON 2134"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("8:00 AM"),
                       tools.time_to_seconds("8:15 AM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        stop2 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        # add stops to routes
        route1.add_stop(stop1)
        route2.add_stop(stop2)

        # add routes to routing calculators
        routingcalculator1.add_route(route1)
        routingcalculator1.add_route(route2)

        # verify that a routing calculator with more than one route is valid
        self.assertTrue(True, routingcalculator1.valid())

    # to test that a routing calculator object is converted to a string correctly
    def test_routing_calculator_to_string(self):
        # initialize routingcalculator object and route object
        routingcalculator1 = RoutingCalculator.RoutingCalculator()
        route1 = RoutingCalculator.Route()

        # initialize stop
        id = 1
        addr = "63 EVERETT ST ALLSTON 2134"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("8:00 AM"),
                       tools.time_to_seconds("8:15 AM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        # add the stop to the route, then add the route to the routing calculator
        route1.add_stop(stop1)
        routingcalculator1.add_route(route1)

        # verify the routing calculator is correctly converted to a string
        self.assertEqual("Route 1: Depot -> ->  Pickup at 63 EVERETT ST ALLSTON 2134, Load(0) Time(8:00 AM, 8:15 AM) "
                         "-> Depot", str(routingcalculator1))

    # to verify the equals method for a routing calculator object
    def test_routing_calculator_equal(self):
        # initialize first routing calculator and first route
        routingcalculator1 = RoutingCalculator.RoutingCalculator()
        route1 = RoutingCalculator.Route()

        # initialize stop
        id = 1
        addr = "63 EVERETT ST ALLSTON 2134"
        pickup = True
        dropoff = False
        time_window = (tools.time_to_seconds("8:00 AM"),
                       tools.time_to_seconds("8:15 AM"))
        curr_load = 0

        stop1 = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        # add the stop to the route, then the route to the routing calculator
        route1.add_stop(stop1)
        routingcalculator1.add_route(route1)

        # initialize second routing calculator
        routingcalculator2 = RoutingCalculator.RoutingCalculator()

        # add route 1 to routingcalculator2
        routingcalculator2.add_route(route1)

        # verify that routingcalculator is equal to routingcalculator2
        self.assertEqual(routingcalculator1, routingcalculator1)


# Test class to test the Travel time callback class
class TestTravelTimeCallBackClass(unittest.TestCase):
    # Test the initializer for travel time callback
    def test_Init(self):
        input = [{"Anchor": "A",
                  "RequestTime": "3:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 43,
                  "PickAddress1": "Brattle St",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2138,
                  "DropHouseNumber": 1184,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446,
                  }]
        locations = [[42.371758, -71.06239], [42.355698, -71.15919], [42.36258, -71.15531]]

        dist_between_locations = RoutingCalculator.CreateDistanceCallback(locations, 3)
        dist_callback = dist_between_locations.Distance
        speed = 25

        travelTimeObject = RoutingCalculator.CreateTravelTimeCallback(dist_callback, speed)

        # check that the travel time object has been initialized properly with a speed of 25
        self.assertEqual(travelTimeObject.speed, 25)

    # test the travel time method for this class
    def test_Travel_Time(self):
        input = [{"Anchor": "A",
                  "RequestTime": "3:00 PM",
                  "Companions": 1,
                  "PickHouseNumber": 43,
                  "PickAddress1": "Brattle St",
                  "Pickcity": "CAMBRIDGE",
                  "pickzip": 2138,
                  "DropHouseNumber": 1184,
                  "DropAddress1": "BEACON ST",
                  "Dropcity": "BROOKLINE",
                  "DropZip": 2446,
                  }]
        locations = [[42.371758, -71.06239], [42.355698, -71.15919], [42.36258, -71.15531]]

        dist_between_locations = RoutingCalculator.CreateDistanceCallback(locations, 3)
        dist_callback = dist_between_locations.Distance
        speed = 25

        # initialize it with dist callback and speed
        travelTimeObject = RoutingCalculator.CreateTravelTimeCallback(dist_callback, speed)

        self.assertTrue(abs(travelTimeObject.TravelTime(0, 1) -
                            (tools.distance(42.371758, -71.06239, 42.355698, -71.15919) * 3600 / 25)) < 10)

# Test Create Distance Callback Class in Routing Calculator
class TestCreateDistanceCallback(unittest.TestCase):

    #Tests initializer and Distance method
    def testDistance(self):
        locations = [[42, -71], (42.37385, -71.12136), (42.344025, -71.11497)]
        num = 3
        distanceCallbackObject = RoutingCalculator.CreateDistanceCallback(locations, num)
        distance0 = distanceCallbackObject.Distance(0,0)
        distance1 = distanceCallbackObject.Distance(0, 1)
        self.assertEqual(distance0, 0)
        self.assertEqual(distance1, 26)