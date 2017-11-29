# This Python file uses the following encoding: utf-8
# Copyright 2015 Tin Arm Engineering AB
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import parser
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
from geopy.distance import great_circle


# we could change this to use the google api
def distance(x1, y1, x2, y2):
    # Great-Circle distance
    return great_circle((x1, y1), (x2, y2)).miles


LOCATIONS = 83


# converts the given time in seconds to a string military time hour, minutes
def secondsToTime(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutesRounded = minutes % 60
    time = 'AM'

    if hours >= 12:
        time = 'PM'
        hours = hours % 12
    if hours == 0:
        hours = 12
    if minutesRounded < 10:
        minutesRounded = '0' + str(minutesRounded)

    return ('{0}:{1} {2}'.format(hours, minutesRounded, time))


# Distance callback

class CreateDistanceCallback(object):
    """Create callback to calculate distances and travel times between points."""

    def __init__(self, locations):
        """Initialize distance array."""
        num_locations = LOCATIONS
        self.matrix = {}

        for from_node in range(num_locations):
            self.matrix[from_node] = {}
            for to_node in range(num_locations):
                x1 = locations[from_node][0]
                y1 = locations[from_node][1]
                x2 = locations[to_node][0]
                y2 = locations[to_node][1]
                self.matrix[from_node][to_node] = distance(x1, y1, x2, y2)

    def Distance(self, from_node, to_node):
        return int(self.matrix[from_node][to_node])


# Demand callback
class CreateDemandCallback(object):
    """Create callback to get demands at location node."""

    def __init__(self, demands):
        self.matrix = demands

    def Demand(self, from_node, to_node):
        return self.matrix[from_node]


# Create the travel time callback (equals distance divided by speed).
class CreateTravelTimeCallback(object):
    """Create callback to get travel times between locations."""

    def __init__(self, dist_callback, speed):
        self.dist_callback = dist_callback
        self.speed = speed

    def TravelTime(self, from_node, to_node):
        travel_time = self.dist_callback(from_node, to_node) / self.speed
        return int(travel_time)


def main(in_dict, geo_file, failure_file):
    # Create the data.
    trip_data = parser.AllTrips(in_dict, geo_file, failure_file)
    print("Running...\n")
    data = [trip_data.locations, trip_data.demands, trip_data.starttimes, trip_data.endtimes]
    locations = data[0]
    demands = data[1]
    start_times = data[2]
    end_times = data[3]
    num_locations = LOCATIONS
    depot = 0
    num_vehicles = 22

    # Create routing model.
    if num_locations > 0:

        routing = pywrapcp.RoutingModel(num_locations, num_vehicles, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        for i in range(2, num_locations, 2):
            routing.AddPickupAndDelivery(i - 1, i)
        # Setting first solution heuristic: the
        # method for finding a first solution to the problem.
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        # Callbacks to the distance function and travel time functions here.
        dist_between_locations = CreateDistanceCallback(locations)
        dist_callback = dist_between_locations.Distance

        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        demands_at_locations = CreateDemandCallback(demands)
        demands_callback = demands_at_locations.Demand
        # Add a dimension for demand.
        slack_max = 0
        vehicle_capacity = 8  # what is the max of the capacity? 8?
        fix_start_cumul_to_zero = True
        demand = "Demand"

        routing.AddDimension(demands_callback, slack_max, vehicle_capacity,
                             fix_start_cumul_to_zero, demand)

        # Adding capacity dimension constraints.
        VehicleCapacity = 8
        NullCapacitySlack = 0
        fix_start_cumul_to_zero = True
        capacity = "Capacity"

        routing.AddDimension(demands_callback, NullCapacitySlack, VehicleCapacity,
                             fix_start_cumul_to_zero, capacity)
        # Add time dimension.
        horizon = 24 * 3600
        time = "Time"
        speed = 25

        travel_times = CreateTravelTimeCallback(dist_callback, speed)
        travel_time_callback = travel_times.TravelTime

        routing.AddDimension(travel_time_callback,  # total time function callback
                             horizon,
                             horizon,
                             fix_start_cumul_to_zero,
                             time)

        # Add time window constraints.
        time_dimension = routing.GetDimensionOrDie(time)
        for location in range(1, num_locations):
            start = start_times[location]
            end = end_times[location]
            time_dimension.CumulVar(location).SetRange(start, end)

        # Solve displays a solution if any.
        assignment = routing.SolveWithParameters(search_parameters)

        if assignment:
            # Solution cost.
            # Inspect solution.
            routes = RoutingCalculator()
            capacity_dimension = routing.GetDimensionOrDie(capacity)
            time_dimension = routing.GetDimensionOrDie(time)

            for vehicle_nbr in range(num_vehicles):
                if not routing.IsVehicleUsed(assignment, vehicle_nbr):
                    continue
                route = Route()
                index = assignment.Value(routing.NextVar(routing.Start(vehicle_nbr)))

                while not routing.IsEnd(index):
                    node_index = routing.IndexToNode(index)
                    load_var = capacity_dimension.CumulVar(index)
                    time_var = time_dimension.CumulVar(index)
                    route.add_stop(Stop(node_index, trip_data.addresses[node_index], node_index % 2 == 1,
                                        (assignment.Min(time_var), assignment.Max(time_var)),
                                        assignment.Value(load_var)))

                    index = assignment.Value(routing.NextVar(index))
                routes.add_route(route)
            if routes.valid():
                print(routes)
                return str(routes)
            else:
                print("Invalid Routes")
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


class Stop:
    def __init__(self, id, addr, pickup, time_window, curr_load):
        self.id = id
        self.pickup = pickup
        self.addr = addr
        self.time_window = time_window
        self.curr_load = curr_load

    def __str__(self):
        return " {pickup_dropoff} at {addr}, Load({load}) Time({tmin}, {tmax})".format(  #
            pickup_dropoff='Pickup' if self.pickup else 'Dropoff',
            addr=self.addr,
            load=self.curr_load,
            tmin=secondsToTime(self.time_window[0]),
            tmax=secondsToTime(self.time_window[1]))


class Route:
    def __init__(self):
        self.depot = None
        self.stops = []

    def add_stop(self, stop):
        self.stops.append(stop)

    def __str__(self):
        return "Depot -> -> {0} -> Depot".format(" -> ".join([str(stop) for stop in self.stops]))

    def valid(self):
        pickups = [stop.id for stop in self.stops if stop.pickup]
        dropoffs = {stop.id for stop in self.stops if not stop.pickup}
        return {p + 1 for p in pickups} == dropoffs


class RoutingCalculator:
    def __init__(self):
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def __str__(self):
        return "\n\n".join(['Route {0}: {1}'.format(i + 1, str(route)) for i, route in enumerate(self.routes)])

    def valid(self):
        return all(route.valid() for route in self.routes)
