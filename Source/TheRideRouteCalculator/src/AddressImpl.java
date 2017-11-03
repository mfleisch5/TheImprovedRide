/**
 * An implementation of an Address. An address has a street, a house number, a city and zip code
 * It is assumed that all addresses are in Massachusetts.
 */
public class AddressImpl implements Address {

    private int houseNumber;
    private String streetName;
    private String city;
    private int zipCode;

    //************DO NOT IMPLEMENT THESE UNTIL UNIT TESTS HAVE BEEN CREATED************

    @Override
    public String getAddress() {
        return null;
    }

    @Override
    public int getHousenumber() {
        return 0;
    }

    @Override
    public String getStreetName() {
        return null;
    }

    @Override
    public String getCity() {
        return null;
    }

    @Override
    public int getZipCode() {
        return 0;
    }
}
