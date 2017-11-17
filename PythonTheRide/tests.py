import unittest


from ortools.constraint_solver import pywrapcp
from RoutingCalculator import secondsToTime, time_to_seconds


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

        self.assertEqual(assignment, 'Route 1:\n Pickup 3:00 PM, Trip ID 1, 149 Sutherland Road, Brighton, 2135\n'
                                     'Dropoff, Trip ID 1, 63 Everett Street, Allston, 2134\n')


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

        self.assertEqual(secondsToTime(time2), '3:30 PM')
        self.assertEqual(secondsToTime(time1), '12:18 AM')
        self.assertEqual(secondsToTime(time3), '12:00 AM')
        self.assertEqual(secondsToTime(time5), '12:01 AM')
        self.assertEqual(secondsToTime(time7), '11:59 AM')
        self.assertEqual(secondsToTime(time8), '11:59 PM')
        self.assertEqual(secondsToTime(time6), '12:09 AM')
        self.assertEqual(secondsToTime(time4), '12:08 AM')
        self.assertEqual(secondsToTime(time9), '12:00 PM')


# to test that the time to seconds converter
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

        self.assertEqual(time_to_seconds(time1), 55800)
        self.assertEqual(time_to_seconds(time2), 1080)
        self.assertEqual(time_to_seconds(time3), 0)
        self.assertEqual(time_to_seconds(time5), 43140)
        self.assertEqual(time_to_seconds(time7), 43740)
        self.assertEqual(time_to_seconds(time8), 480)
        self.assertEqual(time_to_seconds(time6), 86340)
        self.assertEqual(time_to_seconds(time4), 60)
        self.assertEqual(time_to_seconds(time9), 43200)


    def test_Route_CalcuatorExample1(self):
        pickup1 = [42.3674166,-71.1875465] # "127 Main St, WATERTOWN, 2472":
        dropoff1= [42.3139025,-71.0698311] #"73 BIRD ST, DORCHESTER, 2125": "

        pickup2 = [42.3623931,-71.1608296] # "511 ARSENAL ST, WATERTOWN, 2472":
        dropoff2 = [42.3740084,-71.1574514] # "33 DEWEY ST, WATERTOWN, 2472": "

        demands = [2, 1] # number of passengers to pickup (ex: passenger + 1 pca

        start_times = [time_to_seconds("3:00 PM"), time_to_seconds("3:15 PM"), time_to_seconds("3:25 PM"), time_to_seconds("3:40 PM")]

        data = [[pickup1, pickup2, dropoff1, dropoff2] , demands, start_times]  #data array
        locations = data[0]

        # depot is where we start off
        depot = 0

        routing = pywrapcp.RoutingModel(2, 1, depot)

        # Not sure what default search params are
        assignment = routing.SolveWithParameters(pywrapcp.RoutingModel_DefaultSearchParameters)

        self.assertEqual(assignment, 'Route 1:\n Pickup 3:00 PM, Trip ID 1, 149 Sutherland Road, Brighton, 2135\n Dropoff, Trip ID 1, 63 Everett Street, Allston, 2134\n')

# 6 entries
    def test_Route_6Entries(self):

        # these will get bunched into one
        pickup1 = [42.335461,-71.10731299999999]  #"48 FRANCIS ST, BOSTON, 2115": "",
        dropoff1 = [42.387969,-71.12912419999999] # "48 LINCOLN WAY, CAMBRIDGE, 2140": "

        pickup2 = [42.3895516,-71.1299089] #  "24 WALDEN SQUARE RD, CAMBRIDGE, 2140": "",
        dropoff2 = [42.3772638,-71.153024] #"29 ST. SAUVEUR CT, CAMBRIDGE, 2138": "",

        pickup3 = [42.3732528,-71.10397669999999] #"42 MAPLE AVE, CAMBRIDGE, 2139": "",
        dropoff3 = [42.3908234,-71.1089411] #  "235 HIGHLAND AVE, SOMERVILLE, 2143": "",

        # these will get bunched into one

        pickup4 = [42.3443968,-71.0992271] #  "1333 BOYLSTON ST, BOSTON, 2215": "",
        dropoff4 = [42.317529,-71.10611399999999] # "152 CHESTNUT AVE, JAMAICA PLAIN, 2130": "",

        pickup5 = [42.36325739999999,-71.16127709999999] #"498 ARSENAL ST, WATERTOWN, 2472"
        dropoff5 = [42.3623902,-71.1819998] #  "40 CHARLES RIVER RD, WATERTOWN, 2472": "",

        pickup6 = [42.3617706,-71.18177709999999] #"39 CHARLES RIVER RD, WATERTOWN, 2472":
        dropoff6 = [42.3452754,-71.0412235]  #"499 SUMMER ST, BOSTON, 2210": "",

        locations = [pickup1, dropoff1, pickup2, dropoff2, pickup3, dropoff3, pickup4, dropoff4, pickup5, dropoff5, pickup6, dropoff6 ]

        start_times = [time_to_seconds("12:00 PM"), time_to_seconds("12:30 PM"),
                       time_to_seconds("12:15 PM"), time_to_seconds("12:45 PM"),
                       time_to_seconds("2:00 PM"), time_to_seconds("2:30 PM"),
                       time_to_seconds("12:01 PM"), time_to_seconds("1:30 PM"),
                       time_to_seconds("2:00 PM"), time_to_seconds("2:30 PM"),
                       time_to_seconds("3:30 PM"), time_to_seconds("4:15 PM")]

        tw_duration = 1200
        demands = [1, -1, 1, -1]

        end_times = [0] * len(start_times)
        for i in range(len(start_times)):
            end_times[i] = start_times[i] + tw_duration
        data = [locations, demands, start_times, end_times]

        depot = 0

        routing = pywrapcp.RoutingModel(2, 1, depot)

        # Not sure what default search params are
        assignment = routing.SolveWithParameters(pywrapcp.RoutingModel_DefaultSearchParameters)

        self.assertEqual(assignment,
                         'Route 1: Depot ->  Pickup, RideID 1, 48 FRANCIS ST, BOSTON, 2115,\n'
                         'Pickup RideID 2, 24 WALDEN SQUARE RD, CAMBRIDGE, 2140\n'
                         'Dropoff, RideID 1, 48 LINCOLN WAY, CAMBRIDGE, 2140\n'
                         'Dropoff RideID 2, 29 ST. SAUVEUR CT, CAMBRIDGE, 2138\n'
                         'Dropoff RideID 3, 42 MAPLE AVE, CAMBRIDGE, 2139\n'
                         'Route 2: Depot -> Pickup, RideID 4, 1333 BOYLSTON ST, BOSTON, 2215\n'
                         'Dropoff, RideID 4, 152 CHESTNUT AVE, JAMAICA PLAIN, 2130\n'
                         'Pickup, RideID 5, 498 ARSENAL ST, WATERTOWN, 2472\n'
                         'Dropoff, RideID 5, 40 CHARLES RIVER RD, WATERTOWN, 2472\n'
                         'Pickup, RideID 6, 39 CHARLES RIVER RD, WATERTOWN, 2472\n'
                         'Dropoff, RideID 6, 499 SUMMER ST, BOSTON, 2210')


# test two towns trips at the same time
    def test_Route_2DiffTowns(self):

        # these trips are in one area
        pickup1 = [42.310117,-71.057025]  #"135 AUCKLAND ST, DORCHESTER, 2122:",
        dropoff1 = [42.367417,-71.187546] # "125 MAIN ST, WATERTOWN, 2472: "

        #these trips are in another area
        pickup2 = [42.554954,-70.879482] #  "15 CHESTNUT PARK,BEVERLY,1915",
        dropoff2 = [42.416654,-71.104897] #"103 Riverside Ave,MEDFORD,2155",

        locations = [pickup1, dropoff1, pickup2, dropoff2]

        start_times = [time_to_seconds("12:00 PM"), time_to_seconds("12:30 PM"),
                       time_to_seconds("12:00 PM"), time_to_seconds("12:30 PM")]

        tw_duration = 1200
        demands = [1, -1, 1, -1]

        end_times = [0] * len(start_times)
        for i in range(len(start_times)):
            end_times[i] = start_times[i] + tw_duration
        data = [locations, demands, start_times, end_times]

        depot = 0 #where it starts!

        routing = pywrapcp.RoutingModel(2, 1, depot)

        # Not sure what default search params are
        assignment = routing.SolveWithParameters(pywrapcp.RoutingModel_DefaultSearchParameters)

        self.assertEqual(assignment,
                         'Route 1: Depot ->  Pickup, RideID 1, 133 AUCKLAND ST, DORCHESTER, 2122,\n'
                         'Dropoff, RideID 1, 125 MAIN ST, WATERTOWN, 2472\n'
                         'Route 2: Depot -> Pickup, RideID 2, 15 CHESTNUT PARK, BEVERLY,1915\n'
                         'Dropoff, RideID 2, 103 Riverside Ave, MEDFORD, 2155\n')


# test two trips at the same time time in same town, and two trips in another town at same time
    def test_Route_2same_2same(self):

        # these trips are in one area
        pickup1 = [42.310117,-71.057025]  #"133 AUCKLAND ST, DORCHESTER, 2122:",
        dropoff1 = [42.367417,-71.187546] # "125 MAIN ST, WATERTOWN, 2472": "

        pickup2 = [42.288616,-71.062163] # 32 MSGR PATRICK J LYDON WAY,DORCHESTER CENTER,2124
        dropoff2 = [42.395124,-71.079413] #603,Assembly ROW,SOMERVILLE,2145

        #These will go together
        pickup3 = [42.331131, -71.030585]  # 1665,Columbia Rd,S BOSTON,2127
        dropoff3 = [42.340842, -71.081335]  # 568 Columbus Ave,SOUTH END,2118

        pickup4= [42.335793, -71.056021]  # 65,OLD COLONY AVE,SOUTH BOSTON,2127
        dropoff4 = [42.353998, -71.076837]  # "280,CLARENDON ST,BOSTON,2116

        locations = [pickup1, dropoff1, pickup2, dropoff2, pickup3, dropoff3, pickup4, dropoff4]

        start_times = [time_to_seconds("12:00 PM"), time_to_seconds("12:20 PM"),
                       time_to_seconds("12:30 PM"), time_to_seconds("12:45 PM"),
                       time_to_seconds("2:00 PM"), time_to_seconds("2:35 PM"),
                       time_to_seconds("2:15 PM"), time_to_seconds("2:50 PM")]
        tw_duration = 1200
        demands = [1, -1, 1, -1]

        end_times = [0] * len(start_times)
        for i in range(len(start_times)):
            end_times[i] = start_times[i] + tw_duration
        data = [locations, demands, start_times, end_times]

        depot = 0

        routing = pywrapcp.RoutingModel(2, 1, depot)

        # Not sure what default search params are
        assignment = routing.SolveWithParameters(pywrapcp.RoutingModel_DefaultSearchParameters)

        self.assertEqual(assignment,
                         'Route 1: Depot ->  Pickup, RideID 1, 133 AUCKLAND ST, DORCHESTER, 2122,\n'
                         'Dropoff, RideID 1, 125 MAIN ST, WATERTOWN, 2472\n'
                         'Pickup RideID 2, 32 MSGR PATRICK J LYDON WAY, DORCHESTER CENTER, 2124\n'
                         'Dropoff RideID 2, 603 ASSEMBLY ROW, SOMERVILLE, 2145\n'
                         'Route 2: Depot -> Pickup, RideID 4, 1665 COLUMBIA RD, S BOSTON, 2127\n'
                         'Pickup, RideID 5, 65 OLD COLONY AVE, SOUTH BOSTON, 2127\n'
                         'Dropoff, RideID 4, 568 Columbus Ave, SOUTH END, 2118\n'
                         'Dropoff, RideID 5, 280 CLARENDON ST, BOSTON, 2116\n')

# 2 trips, same town, different times, pick up one after the other,
    def test_Route_2trips_sameTown(self):

        # these will get bunched into one, pick up first passenger in Cambridge, pick up second
        # in Cambridge, drop off first passenger in Cambridge, drop off second passenger in Somerville

        pickup1 = [42.3895516,-71.1299089] #  "24 WALDEN SQUARE RD, CAMBRIDGE, 2140": "",
        dropoff1 = [42.3772638,-71.153024] #"29 ST. SAUVEUR CT, CAMBRIDGE, 2138": "",

        pickup2 = [42.3732528,-71.10397669999999] #"42 MAPLE AVE, CAMBRIDGE, 2139": "",
        dropoff2 = [42.3908234,-71.1089411] #  "235 HIGHLAND AVE, SOMERVILLE, 2143": "",

        #not sure if order matters
        locations = [pickup1, pickup2, dropoff1, dropoff2]

        start_times = [time_to_seconds("12:00 PM"), time_to_seconds("12:30 PM"),
                       time_to_seconds("12:15 PM"), time_to_seconds("12:45 PM"),]

        tw_duration = 1200 # max amt of time the passenger can be on the ride
        demands = [1, 1, -1, -1] # pick up pick up drop off drop off

        end_times = [0] * len(start_times)
        for i in range(len(start_times)):
            end_times[i] = start_times[i] + tw_duration
        data = [locations, demands, start_times, end_times]

        depot = 0 # where it starts off

        routing = pywrapcp.RoutingModel(2, 1, depot)

        # Not sure what default search params are
        assignment = routing.SolveWithParameters(pywrapcp.RoutingModel_DefaultSearchParameters)

        self.assertEqual(assignment,
                         'Route 1: Depot ->  Pickup, RideID 1, 24 WALDEN SQUARE RD, CAMBRIDGE, 2140\n'
                         'Pickup RideID 2, 42 MAPLE AVE, CAMBRIDGE, 2139\n'
                         'Dropoff, RideID 1, 29 ST. SAUVEUR CT, CAMBRIDGE, 2138\n'
                         'Dropoff RideID 2, 235 HIGHLAND AVE, SOMERVILLE, 2143\n'
                         )

#4 rides in 4 different towns - at the same time, so separate rides
    def test_Route_4trips4towns_sameTime(self):

        # since they are all at the same time but diff towns, each trip gets a different route

        pickup1 = [42.3895516,-71.1299089] #  "24 WALDEN SQUARE RD, CAMBRIDGE, 2140": "",
        dropoff1 = [42.3772638,-71.153024] #"29 ST. SAUVEUR CT, CAMBRIDGE, 2138": "",

        pickup2 = [42.3409561,-71.1469785] #"149 SUTHERLAND RD, BRIGHTON, 2135": "",
        dropoff2 = [42.356506,-71.1381028] #"66 EVERETT ST, ALLSTON, 2134": "",

        pickup3 = [42.2149672,-71.1842008] #"27 WILSON WAY, WESTWOOD, 2090": "",
        dropoff3 = [42.3495852,-71.2368002] #"25 Larkin Rd, NEWTON, 2465": "",

        pickup4 = [42.3674166,-71.1875465]# "127 Main St, WATERTOWN, 2472": "",
        dropoff4 = [42.3139025,-71.0698311] #"73 BIRD ST, DORCHESTER, 2125": "",

        locations = [pickup1, dropoff1, pickup2, dropoff2, pickup3, dropoff3, pickup4, dropoff4]

        #not sure if the times are right! All are requesting pick up time at 12:00pm
        start_times = [time_to_seconds("12:00 PM"), time_to_seconds("12:10 PM"), #smaller time window since drop off in cambridge
                       time_to_seconds("12:00 PM"), time_to_seconds("12:15 PM"),
                       time_to_seconds("12:00 PM"), time_to_seconds("12:30 PM"),
                       time_to_seconds("12:00 PM"), time_to_seconds("12:45 PM"),]

        tw_duration = 1200 # max amt of time the passenger can be on the ride
        demands = [1, -1, 1, -1, 1, -1, 1, -1] # pick up and drop off separately

        end_times = [0] * len(start_times)
        for i in range(len(start_times)):
            end_times[i] = start_times[i] + tw_duration
        data = [locations, demands, start_times, end_times]

        depot = 0 # where it starts off

        routing = pywrapcp.RoutingModel(2, 1, depot)

        # Not sure what default search params are
        assignment = routing.SolveWithParameters(pywrapcp.RoutingModel_DefaultSearchParameters)

        #each has its own route
        self.assertEqual(assignment,
                         'Route 1: Depot ->  Pickup, RideID 1, 24 WALDEN SQUARE RD, CAMBRIDGE, 2140\n'
                         'Dropoff, RideID 1, 29 ST. SAUVEUR CT, CAMBRIDGE, 2138\n'
                         'Route 2: Depot -> Pickup, RideID 2, 149 SUTHERLAND RD, BRIGHTON, 2135\n'
                         'Dropoff, RideID 2, 66 EVERETT ST, ALLSTON, 2134\n'
                         'Route 3: Depot ->  Pickup, RideID 3, 27 WILSON WAY, WESTWOOD, 2090\n'
                         'Dropoff, RideID 3, 25 Larkin Rd, NEWTON, 2465\n'
                         'Route 4: Depot -> Pickup, RideID 4, 127 Main St, WATERTOWN, 2472\n'
                         'Dropoff, RideID 4, 73 BIRD ST, DORCHESTER, 2125\n'
                         )

if __name__ == '__main__':
    unittest.main()
