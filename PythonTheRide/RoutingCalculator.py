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


# converts the given time in seconds to a string military time hour, minutes
def secondsToTime(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutesRounded = minutes % 60
    time = 'AM'

    if (hours >= 12):
        time = 'PM'
        hours = hours % 12
    if (hours == 0):
        hours = 12
    if (minutesRounded < 10):
        minutesRounded = '0' + str(minutesRounded)

    return ('{0}:{1} {2}'.format(hours, minutesRounded, time))


# Distance callback

class CreateDistanceCallback(object):
    """Create callback to calculate distances and travel times between points."""

    def __init__(self, locations):
        """Initialize distance array."""
        num_locations = 100
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


# Service time (proportional to demand) callback.
class CreateServiceTimeCallback(object):
    """Create callback to get time windows at each location."""

    def __init__(self, demands, time_per_demand_unit):
        self.matrix = demands
        self.time_per_demand_unit = time_per_demand_unit

    def ServiceTime(self, from_node, to_node):
        return int(self.matrix[from_node] * self.time_per_demand_unit)


# Create the travel time callback (equals distance divided by speed).
class CreateTravelTimeCallback(object):
    """Create callback to get travel times between locations."""

    def __init__(self, dist_callback, speed):
        self.dist_callback = dist_callback
        self.speed = speed

    def TravelTime(self, from_node, to_node):
        travel_time = self.dist_callback(from_node, to_node) / self.speed
        return int(travel_time)


# Create total_time callback (equals service time plus travel time).
class CreateTotalTimeCallback(object):
    """Create callback to get total times between locations."""

    def __init__(self, service_time_callback, travel_time_callback):
        self.service_time_callback = service_time_callback
        self.travel_time_callback = travel_time_callback

    def TotalTime(self, from_node, to_node):
        service_time = self.service_time_callback(from_node, to_node)
        travel_time = self.travel_time_callback(from_node, to_node)
        return service_time + travel_time


def main():
    # Create the data.
    data = create_data_array()
    locations = data[0]
    demands = data[1]
    start_times = data[2]
    end_times = data[3]
    num_locations = 100
    depot = 0
    num_vehicles = 150

    # Create routing model.
    if num_locations > 0:

        routing = pywrapcp.RoutingModel(num_locations, num_vehicles, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        """
        for i in range(, num_locations, 2):
            routing.AddPickupAndDelivery(i - 1, i)
        """
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
        """
        # ensure that each node pair is a neighbor
        # def AddPickupAndDelivery(self, node1: 'operations_research::RoutingModel::NodeIndex', node2: 'operations_research::RoutingModel::NodeIndex') -> "void":
        """
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
        time_per_demand_unit = 1
        horizon = 24 * 3600
        time = "Time"
        speed = 1

        service_times = CreateServiceTimeCallback(demands, time_per_demand_unit)
        service_time_callback = service_times.ServiceTime

        travel_times = CreateTravelTimeCallback(dist_callback, speed)
        travel_time_callback = travel_times.TravelTime

        total_times = CreateTotalTimeCallback(service_time_callback, travel_time_callback)
        total_time_callback = total_times.TotalTime

        routing.AddDimension(total_time_callback,  # total time function callback
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
            size = len(locations)
            # Solution cost.
            print("Total distance of all routes: " + str(assignment.ObjectiveValue()) + "\n")
            # Inspect solution.
            capacity_dimension = routing.GetDimensionOrDie(capacity)
            time_dimension = routing.GetDimensionOrDie(time)

            for vehicle_nbr in range(num_vehicles):
                index = routing.Start(vehicle_nbr)
                plan_output = 'Route {0}:'.format(vehicle_nbr + 1)

                while not routing.IsEnd(index):
                    node_index = routing.IndexToNode(index)
                    load_var = capacity_dimension.CumulVar(index)
                    time_var = time_dimension.CumulVar(index)

                    if node_index == 0:
                        plan_output += \
                            " Depot ->  -> ".format(  # {node_index} Load({load}) Time({tmin}, {tmax})
                                node_index=node_index,
                                load=assignment.Value(load_var),
                                tmin=secondsToTime(assignment.Min(time_var)),  # str
                                tmax=secondsToTime(assignment.Max(time_var)))
                    else:

                        pickup_dropoff1 = str('Dropoff') if node_index % 2 == 1 else str('Pickup')

                        plan_output += \
                            " {pickup_dropoff}, RideID {node_index}, Load({load}) Time({tmin}, {tmax}) -> ".format(  #
                                pickup_dropoff=pickup_dropoff1,
                                node_index=node_index,
                                load=assignment.Value(load_var),
                                tmin=secondsToTime(assignment.Min(time_var)),
                                tmax=secondsToTime(assignment.Max(time_var)))

                    index = assignment.Value(routing.NextVar(index))

                node_index = routing.IndexToNode(index)
                load_var = capacity_dimension.CumulVar(index)
                time_var = time_dimension.CumulVar(index)
                plan_output += \
                    " Depot"  # RouteID {node_index}  Time({tmin}, {tmax})".format( #Load({load})
                # node_index=node_index,
                # load=assignment.Value(load_var),
                # tmin=secondsToTime(assignment.Min(time_var)),
                # tmax=secondsToTime(assignment.Max(time_var)))
                print(plan_output)
                print("\n")
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


def create_data_array():
    data = parser.AllTrips('../Data.csv', 'geocodes.json', 'failures.json')
    data.testIt()
    locations = data.locations
    start_times = data.starttimes
    end_times = data.endtimes
    demands = data.demands

    data_array = [locations, demands, start_times, end_times]

    return data_array

if __name__ == '__main__':
    main()
