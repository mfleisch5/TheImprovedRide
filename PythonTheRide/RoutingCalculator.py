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

import ortools
import parser
import math
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# we could change this to use the google api
def distance(x1, y1, x2, y2):
       # Manhattan distance
    dist = abs(x1 - x2) + abs(y1 - y2)

    return dist

# converts the given time in seconds to a string military time hour, minutes
def secondsToTime(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutesRounded = minutes % 60
    time = 'AM'

    if(hours >= 12):
        time = 'PM'
        hours = hours % 12
    if (hours == 0):
        hours = 12
    if(minutesRounded < 10):
        minutesRounded = '0' + str(minutesRounded)

    return ('{0}:{1} {2}'.format(hours, minutesRounded, time))


# Distance callback
class CreateDistanceCallback(object):
  """Create callback to calculate distances and travel times between points."""

  def __init__(self, locations):
    """Initialize distance array."""
    num_locations = 12
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
  num_locations = len(locations)
  depot = 0
  num_vehicles = 400
  search_time_limit = 400000

  # Create routing model.
  if num_locations > 0:

    # The number of nodes of the VRP is num_locations.
    # Nodes are indexed from 0 to num_locations - 1. By default the start of
    # a route is node 0.
    routing = pywrapcp.RoutingModel(num_locations, num_vehicles, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters() #search_parameters = pywrapcp.RoutingModel.DefaultRoutingSearchParameters()

    # Callbacks to the distance function and travel time functions here.
    dist_between_locations = CreateDistanceCallback(locations)
    dist_callback = dist_between_locations.Distance

    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    demands_at_locations = CreateDemandCallback(demands)
    demands_callback = demands_at_locations.Demand

    #ensure that each node pair is a neighbor

    # def AddPickupAndDelivery(self, node1: 'operations_research::RoutingModel::NodeIndex', node2: 'operations_research::RoutingModel::NodeIndex') -> "void":
    routing.AddPickupAndDelivery(0, 1)
    routing.AddPickupAndDelivery(2, 3)
    routing.AddPickupAndDelivery(4, 5)
    routing.AddPickupAndDelivery(6, 7)
    routing.AddPickupAndDelivery(8, 9)
    routing.AddPickupAndDelivery(10, 11)


    # Add a dimension for demand.
    slack_max = 0
    vehicle_capacity = 100  #what is the max of the capacity? 8?
    fix_start_cumul_to_zero = True
    demand = "Demand"
    routing.AddDimension(demands_callback, slack_max, vehicle_capacity,
                         fix_start_cumul_to_zero, demand)

    # Adding capacity dimension constraints.
    VehicleCapacity = 100
    NullCapacitySlack = 0
    fix_start_cumul_to_zero = True
    capacity = "Capacity"

    routing.AddDimension(demands_callback, NullCapacitySlack, VehicleCapacity,
                         fix_start_cumul_to_zero, capacity)
    # Add time dimension.
    time_per_demand_unit = 3
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
    # routing.AddDimension()

    # Add time window constraints.
    time_dimension = routing.GetDimensionOrDie(time)
    for location in range(1, num_locations):
      start = start_times[location]
      end = end_times[location]
      print(start, end)
      time_dimension.CumulVar(location).SetRange(start, end)


    # Solve displays a solution if any.
    assignment = routing.SolveWithParameters(search_parameters)  #have a time out exception here....?
    if assignment:
      size = len(locations)
      # Solution cost.
      print ("Total distance of all routes: " + str(assignment.ObjectiveValue()) + "\n")
      # Inspect solution.
      capacity_dimension = routing.GetDimensionOrDie(capacity);
      time_dimension = routing.GetDimensionOrDie(time);

      for vehicle_nbr in range(num_vehicles):
        index = routing.Start(vehicle_nbr)
        plan_output = 'Route {0}:'.format(vehicle_nbr + 1)

        while not routing.IsEnd(index):
          node_index = routing.IndexToNode(index)
          load_var = capacity_dimension.CumulVar(index)
          time_var = time_dimension.CumulVar(index)

          if (node_index == 0):
              plan_output += \
                    " Depot ->  -> ".format( #{node_index} Load({load}) Time({tmin}, {tmax})
                        node_index=node_index,
                        load= assignment.Value(load_var),
                        tmin=secondsToTime(assignment.Min(time_var)), #str
                        tmax= secondsToTime(assignment.Max(time_var)))
          else:

              if (node_index % 2 == 1):
                  pickup_dropoff1 = str('Dropoff')
              else: pickup_dropoff1 = str('Pickup')

              plan_output += \
                  " {pickup_dropoff}, RideID {node_index}, Load({load}) Time({tmin}, {tmax}) -> ".format( #
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
                  " Depot" #RouteID {node_index}  Time({tmin}, {tmax})".format( #Load({load})
                      # node_index=node_index,
                      # load=assignment.Value(load_var),
                      # tmin=secondsToTime(assignment.Min(time_var)),
                      # tmax=secondsToTime(assignment.Max(time_var)))
        print (plan_output)
        print ("\n")
    else:
      print ('No solution found.')
  else:
    print ('Specify an instance greater than 0.')


def create_data_array():
    data = parser.AllTrips('MockData.csv')
    locations = data.locations
    start_times = data.starttimes
    end_times = data.endtimes
    # these will get bunched into one
    """
    locations = [[42.335461, -71.10731299999999],
                 [42.387969, -71.12912419999999],
                 [42.3895516, -71.1299089],
                 [42.3772638, -71.153024],
                 [42.3732528, -71.10397669999999],
                 [42.3908234, -71.1089411],
                 [42.3443968, -71.0992271],
                 [42.317529, -71.10611399999999],
                 [42.36325739999999, -71.16127709999999],
                 [42.3623902, -71.1819998],
                 [42.3617706, -71.18177709999999],
                 [42.3452754, -71.0412235]]

    start_times = [time_to_seconds("12:00 PM"), time_to_seconds("12:30 PM"),
                   time_to_seconds("12:15 PM"), time_to_seconds("12:45 PM"),
                   time_to_seconds("2:00 PM"), time_to_seconds("2:30 PM"),
                   time_to_seconds("12:01 PM"), time_to_seconds("1:30 PM"),
                   time_to_seconds("2:01 PM"), time_to_seconds("2:31 PM"),
                   time_to_seconds("3:30 PM"), time_to_seconds("4:15 PM")]


    end_time = [time_to_seconds("12:15 PM"), time_to_seconds("12:40 PM"),
                   time_to_seconds("12:15 PM"), time_to_seconds("12:45 PM"),
                   time_to_seconds("2:00 PM"), time_to_seconds("2:30 PM"),
                   time_to_seconds("12:01 PM"), time_to_seconds("1:30 PM"),
                   time_to_seconds("2:01 PM"), time_to_seconds("2:31 PM"),
                   time_to_seconds("3:30 PM"), time_to_seconds("4:15 PM")]
    """
    tw_duration = 0
    demands = data.demands
    data = [locations, demands, start_times, end_times]

    return data



# locations = [[820, 760], [960, 440], [500, 50], [490, 80], [130, 70], [290, 890], [580, 300],
  #              [840, 390], [140, 240], [120, 390], [30, 820], [50, 100], [980, 520], [840, 250],
  #              [610, 590], [10, 650], [880, 510], [910, 20], [190, 320], [930, 30], [500, 930],
  #              [980, 140], [50, 420], [420, 90], [610, 620], [90, 970], [800, 550], [570, 690],
  #              [230, 150], [200, 700], [850, 600], [980, 50]]
  #
  # demands =  [0, 19, 21, 6, 19, 7, 12, 16, 6, 16, 8, 14, 21, 16, 3, 22, 18,
  #            19, 1, 24, 8, 12, 4, 8, 24, 24, 2, 20, 15, 2, 14, 9]
  #
  # start_times =  [0, 508, 103, 493, 225, 531, 89,
  #                 565, 540, 108, 602, 466, 356, 303,
  #                 399, 382, 362, 521, 23, 489, 445,
  #                 318, 380, 55, 574, 515, 110, 310,
  #                 387, 491, 328, 73]

  # tw_duration is the width of the time windows.
  #tw_duration = 2150

  # In this example, the width is the same at each location, so we define the end times to be
  # start times + tw_duration. For problems in which the time window widths vary by location,
  # you can explicitly define the list of end_times, as we have done for start_times.

if __name__ == '__main__':
  main()