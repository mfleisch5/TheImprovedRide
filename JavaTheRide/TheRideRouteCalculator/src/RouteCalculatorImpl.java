import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;



/**
 * An implementation of a Route Calculator.
 */
public class RouteCalculatorImpl implements RouteCalculator {

    private List<Trip> listofTrips;

    public RouteCalculatorImpl(List<Trip> listOfTrips) {

    }

    // Create a Route Calculator based on the file name given
    public RouteCalculatorImpl(String name) {

        List<Trip> listofTrips = new ArrayList<Trip>();
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(name));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        Scanner scanner = new Scanner(br);
        while (scanner.hasNext()) {
            String lineType = scanner.next();
            String[] values = lineType.split(",");

            if (values.length != 16) {
                continue;
            }

            Trip t = new TripImpl(Integer.parseInt(values[0]), values[1].equals("Y"),
                    values[2].equals("ADA"), values[3].equals("P"),
                    values[4], Integer.parseInt(values[5]), Integer.parseInt(values[6]), values[7].equals("Y"),
                    new AddressImpl(Integer.parseInt((values[8])), values[9], values[10], Integer.parseInt(values[11])),
                    new AddressImpl(Integer.parseInt(values[12]), values[13], values[14], Integer.parseInt(values[15])), 0);

            listofTrips.add(t);
    }

    this.listofTrips = listofTrips;
    }

    private String routeSchedule;

    //************DO NOT IMPLEMENT THESE UNTIL UNIT TESTS HAVE BEEN CREATED************


    public void routeCalculator() {

    }


    @Override
    public String outPutRoutes() {
        return null;
    }

    private class Route {

        public List<Trip> tripsInRoute;
        public String instructions;

        public Route(Trip firstTrip, int rideID) {
            tripsInRoute = new ArrayList<Trip>();
            tripsInRoute.add(firstTrip);
            instructions = "";
        }
        public void addTrip(Trip toAdd) {
            tripsInRoute.add(toAdd);
            instructions += "Pick up: " + toAdd.toString(true);
        }

        public void completeTrip(Trip toComplete) {
            instructions += "Drop off: " + toComplete.toString(false);

        }

    }
}
