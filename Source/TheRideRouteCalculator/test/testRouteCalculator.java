import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;

/**
 * To test the RouteCalculator interface and it's implementing classes.
 */
public class testRouteCalculator {

    /**
     * Tests the route calculator for input where 4 trips are scheduled in the same town, but all at different times.
     */
    @Test
    public void testFourTripsSameTownDiffTimes(){

        Address pickup1 = new AddressImpl(345, "Washington Street", "Westwood", 2090);
        Address dropoff1 = new AddressImpl(46, "Peartree Drive", "Westwood", 2090);

        Address pickup2 = new AddressImpl(43, "Peartree Drive", "Westwood", 2090);
        Address dropoff2 = new AddressImpl(342, "Washington Street", "Westwood", 2090);

        Address pickup3 = new AddressImpl(95, "Glacier Drive", "Westwood", 2090);
        Address dropoff3 = new AddressImpl(1330, "Highland Glen Road", "Westwood", 2090);

        Address pickup4 = new AddressImpl(1331, "Highland Glen Drive", "Westwood", 2090);
        Address dropoff4 = new AddressImpl(96, "Glacier Drive", "Westwood", 2090);

        // Same trip ID to denote ride sharing
        Trip trip1 = new TripImpl(2532, true, true, true, "6:15 PM",
                0, 0, false, pickup1, dropoff1);

        Trip trip2 = new TripImpl(2533, true, true, false, "8:45 AM",
                0, 0, false, pickup2, dropoff2);

        Trip trip3 = new TripImpl(3077, false, true, true, "10:30 AM",
                0, 0, false, pickup3, dropoff3);

        Trip trip4 = new TripImpl(3078, false, true, false, "6:00 AM",
                0, 0, false, pickup4, dropoff4);

        List<Trip> trips = new ArrayList<Trip>();
        trips.add(trip1);
        trips.add(trip2);
        trips.add(trip3);
        trips.add(trip4);

        RouteCalculator calc = new RouteCalculatorImpl(trips);

        // calculate a schedule
        calc.routeCalculator();

        String answer = "Route:\n" +
                "Pickup 6:00 AM, Trip ID 3078, 1331 Highland Glen Drive , Westwood, 2090\n" +
                "Dropoff, Trip ID 3078, 96 Glacier Drive, Westwood, 2090" +
                "Pickup 6:45 AM, Trip ID 3077, 95 Glacier Drive, Westwood, 2090\n" +
                "Dropoff, Trip ID 2533, 1330 Highland Glen Road, Westwood, 2090\n" +
                "Pickup 7:30 AM, Trip ID 2532, 345 Washington Street, Westwood, 2090\n" +
                "Dropoff, Trip ID 2532, 46 Peartree Drive, Westwood, 2090\n" +
                "Pickup 8:45 AM, Trip ID 2533, 43 Peartree Drive, Westwood, 2090\n" +
                "Dropoff, Trip ID 2533, 342 Washington Street, Wetwood, 2090\n";

        assertEquals("Expected output schedule should match calculated one", answer, calc.outPutRoutes());

    }
}
