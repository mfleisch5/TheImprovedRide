/**
 * Interface to represent a single trip in a route.
 * This is based off of a single row in the sample data set.
 */
public interface Trip {

    /**
     * To return the trip ID of a scheduled trip
     * @return int
     */
    public int getTripID();

    /**
     * Does the person on this trip have a subscription?
     * @return boolean
     */
    public boolean getSubscription();

    /**
     * Determines if the ride is ADA or non-ADA. Returning true indicates AFA, false indicates non-ADA
     * @return boolean
     */
    public boolean getADA();

    /**
     * Determines the time anchor of the ride. True indicates the time is pickup, false indicates the time is
     * arrival.
     * (For example, if my pickup time is 12pm, this function returns true as that is teh specified pickup
     * if I specify my time is 12pm arrival at destination, this function returns false as I am specifying a
     * arrival time.
     * @return boolean
     */
    public boolean getAnchor();

    /**
     * Returns the request time
     * @return String
     */
    public String getRequestTime();

    /**
     * Returns the number of personal care assistances that are accompanying this trip. Cannot be less
     * that 0.
     * @return int
     */
    public int getPcas();

    /**
     * Returns the number of companions accompanying this trip. Cannot be less than 0.
     * @return int
     */
    public int getCompanions();

    /**
     * Does the rider have a service animal? True if yes, false if no.
     * @return boolean
     */
    public boolean getServiceAnimal();

    /**
     * Return the Address of the pickup location. This returns an Address object.
     * @return Address
     */
    public Address getPickup();

    /**
     * Return the Address of teh dropoff location. This returns an Address object.
     * @return
     */
    public Address getDropoff();


    /**
     * Return the Ride Id of this trip.
     * @return
     */
    public int getRideID();
}
