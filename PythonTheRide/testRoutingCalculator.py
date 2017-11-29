import unittest
import RoutingCalculator


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
        routes = RoutingCalculator.main(input, 'geocodes.json', 'failures.json', 3)
        self.assertEqual(str(routes), "Route 1: Depot -> ->  Pickup at 43 Brattle St CAMBRIDGE 2138, Load(0) " +
                                      "Time(2:34 PM, 2:54 PM) ->  Dropoff at 1184 BEACON ST BROOK" +
                                      "LINE 2446, Load(2) Time(2:40 PM, 3:00 PM) -> Depot")
