import unittest

from ortools.constraint_solver import pywrapcp


class TestRouteCalculator(unittest.TestCase):

    def test_upper(self):
        # Once the methods are done, we pass in the actual address and use a geocode method
        # to convert it to lat/long
        #
        # pickaddress1 = "149 Sutherland Road Brighton 2135"
        # dropoffaddress1 = "63 Everett Street Allston 2134"

        pickup1 = [42.3409561, -71.14697849999999]
        dropoff1 = [42.3557609, -71.1382691]

        demands = 2 # number of passengers to pickup (ex: passenger + 1 pca

        # Start time in seconds. For example this is 3:00 PM. Once we have a method, we will conver the time
        # into seconds (Military Time!!)
        #
        # pickuptime1 = "3:00 PM"

        start_times = 54000

        data = [[pickup1][dropoff1] , demands, start_times]  #data array
        locations = data[0]

        # depot is where we start off
        depot = 0

        routing = pywrapcp.RoutingModel(2, 1, depot)

        # Not sure what deault search params are
        assignment = routing.SolveWithParameters(pywrapcp.RoutingModel_DefaultSearchParameters)

        self.assertEqual(assignment, 'Route 1:\n Pickup 3:00 PM, Trip ID 1, 149 Sutherland Road, Brighton, 2135\n Dropoff, Trip ID 1, 63 Everett Street, Allston, 2134\n')

if __name__ == '__main__':
    unittest.main()