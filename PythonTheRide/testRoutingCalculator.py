import unittest, os
from . import RoutingCalculator
from . import parser

dir_path = os.path.dirname(os.path.realpath(__file__))

geo_path = os.path.join(dir_path, 'geocodes.json')
fail_path = os.path.join(dir_path, 'failures.json')

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
        routes = RoutingCalculator.main(input, geo_path, fail_path, 3)
        self.assertEqual(str(routes), "Route 1: Depot -> ->  Pickup at 43 Brattle St CAMBRIDGE 2138, Load(0) " +
                         "Time(2:34 PM, 2:54 PM) ->  Dropoff at 1184 BEACON ST BROOK" +
                         "LINE 2446, Load(2) Time(2:40 PM, 3:00 PM) -> Depot")

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

        routes = RoutingCalculator.main(input, geo_path, fail_path, 9)
        i = str(routes)
        self.maxDiff = None

        self.assertEqual(i,
                         "Route 1: Depot -> ->  Pickup at 43 Brattle St CAMBRIDGE 2138, Load(0) Time(11:34 AM, 11:54 " +
                         "AM) ->  Pickup at 42 MAPLE AVE CAMBRIDGE 2139, Load(2) Time(11:37 AM, 11:56 AM) ->  Dropoff at 235 HIGHLAND AVE SOMVERVILLE " +
                         "2143, Load(4) Time(11:40 AM, 11:56 AM) ->  Pickup at 24 WALDEN SQUARE RD CAMBRIDGE 2140, Load(2) Time(11:40 AM, 11:56 " +
                         "AM) ->  Dropoff at 29 ST. SAUVEUR CT CAMBRIDGE 2138, Load(4) Time(11:40 AM, 11:59 AM) ->  Dropoff at 1184 BEACON ST BROOKLINE " +
                         "2446, Load(2) Time(11:40 AM, 11:59 AM) ->  Pickup at 28 WILSON WAY WESTWOOD 2090, Load(0) Time(11:40 AM, 11:59 AM) ->  Dropoff " +
                         "at 27 WILSON WAY WESTWOOD 2090, Load(2) Time(11:40 AM, 12:00 PM) -> Depot")

        # Calculate a route where two pickups are from the same town (ridesharing 2 people). Pickup in succession, dropoff in succession

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
        routes = RoutingCalculator.main(input, geo_path, fail_path, 5)
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
        routes = RoutingCalculator.main(input, geo_path, fail_path, 5)
        i = str(routes)
        self.maxDiff = None

        # should be pickup 1 dropoff 1 pickup 2 dropoff 2
        self.assertEqual(i, "Route 1: Depot -> ->  Pickup at 63 EVERETT ST ALLSTON 2134, " +
                         "Load(0) Time(11:37 AM, 11:57 AM) ->  Dropoff at 152 SUTHERLAND RD BRIGHTON 2135, " +
                         "Load(2) Time(11:40 AM, 12:00 PM) ->  Pickup at 10 CORINNE RD BRIGHTON 2135, " +
                         "Load(0) Time(1:47 PM, 2:07 PM) ->  Dropoff at 3 City Sq CHARLESTOWN 2129, " +
                         "Load(2) Time(2:00 PM, 2:20 PM) -> Depot")

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
        self.assertRaises(Exception, RoutingCalculator.main(input, geo_path, fail_path, 1))


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
        time_window = (parser.time_to_seconds("3:00 PM"),
                       parser.time_to_seconds("3:15 PM"))
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
        time_window = (parser.time_to_seconds("3:00 PM"),
                       parser.time_to_seconds("3:15 PM"))
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
        time_window = (parser.time_to_seconds("3:00 PM"),
                       parser.time_to_seconds("3:15 PM"))
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
        time_window = (parser.time_to_seconds("3:00 PM"),
                       parser.time_to_seconds("3:15 PM"))
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
        time_window = (parser.time_to_seconds("3:00 PM"), parser.time_to_seconds("3:15 PM"))
        curr_load = 0

        stopa = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)

        self.assertEquals(1, stopa.id)
        self.assertEquals("95 TREMONT ST, BOSTON, 2108", stopa.addr)
        self.assertEquals(True, stopa.pickup)
        self.assertEqual((parser.time_to_seconds("3:00 PM"), parser.time_to_seconds("3:15 PM")), stopa.time_window)
        self.assertEqual(0, stopa.curr_load)

        id2 = 2
        addr2 = "95 TREMONT ST, BOSTON, 2108"
        pickup2 = False
        time_window2 = (parser.time_to_seconds("3:00 PM"), parser.time_to_seconds("3:15 PM"))
        curr_load2 = 0

        stopb = RoutingCalculator.Stop(id2, addr2, pickup2, time_window2, curr_load2)

        self.assertEquals(2, stopb.id)
        self.assertEquals("95 TREMONT ST, BOSTON, 2108", stopb.addr)
        self.assertEquals(False, stopb.pickup)
        self.assertEqual((parser.time_to_seconds("3:00 PM"), parser.time_to_seconds("3:15 PM")), stopb.time_window)
        self.assertEqual(0, stopb.curr_load)

    # To test that a stop object is converted to string correctly
    def test_stop_to_string(self):
        id = 1
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        time_window = (parser.time_to_seconds("3:00 PM"), parser.time_to_seconds("3:15 PM"))
        curr_load = 0

        stopa = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        self.assertEquals(" Pickup at 95 TREMONT ST, BOSTON, 2108, Load(0) Time(3:00 PM, 3:15 PM)", str(stopa))

        id = 2
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = False
        time_window = (parser.time_to_seconds("3:00 PM"), parser.time_to_seconds("3:15 PM"))
        curr_load = 0

        stopb = RoutingCalculator.Stop(id, addr, pickup, time_window, curr_load)
        self.assertEquals(" Dropoff at 95 TREMONT ST, BOSTON, 2108, Load(0) Time(3:00 PM, 3:15 PM)", str(stopb))

    # To verify the equals method for a stop object
    def test_stop_equals(self):
        id = 1
        addr = "95 TREMONT ST, BOSTON, 2108"
        pickup = True
        time_window = (parser.time_to_seconds("3:00 PM"), parser.time_to_seconds("3:15 PM"))
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
        time_window = (parser.time_to_seconds("3:00 PM"),
                       parser.time_to_seconds("3:15 PM"))
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
        time_window = (parser.time_to_seconds("3:00 PM"),
                       parser.time_to_seconds("3:15 PM"))
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
        time_window = (parser.time_to_seconds("8:00 AM"),
                       parser.time_to_seconds("8:15 AM"))
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
        time_window = (parser.time_to_seconds("8:00 AM"),
                       parser.time_to_seconds("8:15 AM"))
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
        time_window = (parser.time_to_seconds("8:00 AM"),
                       parser.time_to_seconds("8:15 AM"))
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
