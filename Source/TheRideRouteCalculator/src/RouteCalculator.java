/**
 * Main interface to output String of all routes.
 */

public interface RouteCalculator {

    /**
     * Calculate all trips of the route. Once the route has been calculated, it should be stored in some
     * local field.
     */
    public void routeCalculator();

    /**
     * Retrieve a string containing all routes.
     * If no route has been calculated, calculate the routes.
     * @return String of the outputted routes.
     */
    public String outPutRoutes();

}
