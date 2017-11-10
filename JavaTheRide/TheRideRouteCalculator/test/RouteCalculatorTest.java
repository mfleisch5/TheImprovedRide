import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class RouteCalculatorTest {

    @Test
    public void testTripsFourTowns() {

        Address pickup1 = new AddressImpl(149, "Sutherland Road", "Brighton", 2135);
        Address dropoff1 = new AddressImpl(63, "Everett Street", "allston", 2134);

        Address pickup2 = new AddressImpl(657, "Huntington Avenue", "Boston", 2115);
        Address dropoff2 = new AddressImpl(303, "State Street", "Boston", 2109);

        Address pickup3 = new AddressImpl(101, "Independence Way", "Danvers", 1923);
        Address dropoff3 = new AddressImpl(181, "Newbury Street", "Danvers", 1923);

        Address pickup4 = new AddressImpl(6, "Rubin Court", "Canton", 2021);
        Address dropoff4 = new AddressImpl(306, "Walpole Street", "Norwood", 2062);

        Trip trip1 = new TripImpl(1, false, true, true,
                        "3:00 PM", 1, 0, false, pickup1, dropoff1, 1);

        Trip trip2 = new TripImpl(26, false, true, false, "10:00 AM",
                1, 0, false, pickup2, dropoff2, 12);

        Trip trip3 = new TripImpl(12, false, false, true, "11:15 PM",
                0, 0, false, pickup3, dropoff3, 35);

        Trip trip4 = new TripImpl(27, false, true, false, "2:00 PM",
                0, 0, false, pickup4, dropoff4, 5);

        List<Trip> trips = new ArrayList<Trip>();
        trips.add(trip1);
        trips.add(trip2);
        trips.add(trip3);
        trips.add(trip4);

        RouteCalculator calculator = new RouteCalculatorImpl(trips);

        // Calculate a schedule
        calculator.routeCalculator();

        //output contains pickup request time, address, tripID
        // pickup request time, address tripid
        //dropof trip id, address
        String answer = "Route 1:\n" +
                "Pickup 3:00 PM, Trip ID 1, 149 Sutherland Road, Brighton, 2135\n" +
                "Dropoff, Trip ID 1, 63 Everett Street, Allston, 2134\n" +
                "Route 2:\n" +
                "Pickup 10:AM, Trip ID 26, 657 Huntington Avenue, Boston 2115\n" +
                "Dropoff, Trip ID 26, 303 State Street, Boston 2109\n" +
                "Route 3:\n" +
                "Pickup 11:15 AM, Trip ID 12, 101 Independence Way, Danvers, 1923\n" +
                "Dropoff, Trip ID 12, 181 Newbury Street, Danvers 1923\n" +
                "Route 4:\n" +
                "Pickup 2:00 PM, Trip ID 27, 6 Rubin Court, Canton, 2021\n" +
                "Dropoff, Trip ID 27, 306 Walpole Street, Norwood 2062";

        assertEquals("Expected output schedule should match calculated one",
                answer, calculator.outPutRoutes());

    }

    /**
     * Tests the route calculator for input where 4 trips are scheduled at the same time, 2 of which are in the same
     * town and going to nearby destinations and the other 2 are in a different town, going to the same destination
     */
    @Test
    public void testTripsTwoSameTwoDiffTowns() {
        Address pickup1 = new AddressImpl(149, "Sutherland Road", "Brighton", 2135);
        Address dropoff1 = new AddressImpl(63, "Everett Street", "Allston", 2134);

        Address pickup2 = new AddressImpl(55, "Cummings Road", "Brighton", 2135);
        Address dropoff2 = new AddressImpl(98, "Saunders Street", "Allston", 2134);

        Address pickup3 = new AddressImpl(21, "High Street", "Hingham", 2043);
        Address dropoff3 = new AddressImpl(2, "Pond Park Road", "Hingham", 2043);


        Address pickup4 = new AddressImpl(150, "Prospect Street", "Hingham", 2043);
        Address dropoff4 = new AddressImpl(2, "Pond Park Road", "Hingham", 2043);


        // Same Ride ID to denote RIDE SHARING
        Trip trip1 = new TripImpl(1, false, false, true,
                "3:00 PM", 1, 0, false, pickup1, dropoff1, 14);

        Trip trip2 = new TripImpl(14, false, true, false, "3:05 PM",
                1, 0, false, pickup2, dropoff2, 14);

        Trip trip3 = new TripImpl(22, false, false, true, "11:15 AM",
                0, 0, false, pickup3, dropoff3, 23);

        Trip trip4 = new TripImpl(14, false, true, false, "11:15 AM",
                0, 0, false, pickup4, dropoff4, 23);


        List<Trip> trips = new ArrayList<Trip>();
        trips.add(trip1);
        trips.add(trip2);
        trips.add(trip3);
        trips.add(trip4);

        RouteCalculator calculator = new RouteCalculatorImpl(trips);

        // Calculate a schedule
        calculator.routeCalculator();


        String answer = "Route 1:\n" +
                "Pickup 3:00 PM, Trip ID 1, 149 Sutherland Road, Brighton, 2135\n" +
                "Dropoff, Trip ID 1, 63 Everett Street, Allston, 2134\n" +
                "Route 2:\n" +
                "Pickup 3:05P M, Trip ID 14, 55 Cummings Road, Brighton, 2135\n" +
                "Dropoff, Trip ID 14, 98 Saunders Street, Allston, 2134\n" +
                "Route 3:\n" +
                "Pickup 11:15 AM, Trip ID 22, 21 High Street, Hingham, 2043\n" +
                "Dropoff, Trip ID 22, 2 Pond Park Road, Hingham, 2043\n" +
                "Route 4:\n" +
                "Pickup 2:00 PM, Trip ID 14, 150 Prospect Street , Hingham, 2043\n" +
                "Dropoff, Trip ID 14, 2 Pond Park Road, Hingham, 2043";

        assertEquals("Expected output schedule should match calculated one",
                answer, calculator.outPutRoutes());
    }

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
                0, 0, false, pickup1, dropoff1, 1);

        Trip trip2 = new TripImpl(2533, true, true, false, "8:45 AM",
                0, 0, false, pickup2, dropoff2, 2);

        Trip trip3 = new TripImpl(3077, false, true, true, "10:30 AM",
                0, 0, false, pickup3, dropoff3, 3);

        Trip trip4 = new TripImpl(3078, false, true, false, "6:00 AM",
                0, 0, false, pickup4, dropoff4, 4);

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