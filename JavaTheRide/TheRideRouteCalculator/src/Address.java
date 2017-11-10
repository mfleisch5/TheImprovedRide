import java.net.MalformedURLException;

/**
 * Interface to represent an address in a trip.
 */

public interface Address {

    /**
     * Retrieve the address.
     * @return The complete address including house number, street name, city, and zip code.
     */
    public String getAddress();

    /**
     * Retrieve the house number of the address.
     * @return The house number as an integer.
     */
    public int getHousenumber();

    /**
     * Retrieve the street name of the address.
     * @return The street name as a String.
     */
    public String getStreetName();

    /**
     * Retrieve the city of the address.
     * @return The city as a String.
     */
    public String getCity();

    /**
     * Retrieve the zip code of the address.
     * @return The zip code as an integer.
     */
    public int getZipCode();

    public String getGeoCode() throws Exception;

}
