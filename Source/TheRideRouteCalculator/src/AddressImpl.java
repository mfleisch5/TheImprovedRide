import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import javax.xml.parsers.DocumentBuilderFactory;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.StringJoiner;

/**
 * An implementation of an Address. An address has a street, a house number, a city and zip code
 * It is assumed that all addresses are in Massachusetts.
 */
public class AddressImpl implements Address {

    private static final String GOOGLEKEY = "AIzaSyBF3pvalcQ0fdP9FjdPjTiL2T4YQMnvHps";
    private int houseNumber;
    private String streetName;
    private String city;
    private int zipCode;

    //************DO NOT IMPLEMENT THESE UNTIL UNIT TESTS HAVE BEEN CREATED************

    public AddressImpl(int houseNum, String stName, String city, int zC) {
        this.houseNumber = houseNum;
        this.streetName =stName;
        this.city = city;
        this.zipCode = zC;
    }

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

    @Override
    public String getGeoCode() throws Exception {
        String workingURL = "https://maps.googleapis.com/maps/api/geocode/xml?address=" +
                new StringJoiner("+").add("" + this.houseNumber).add(this.streetName)
                .add(this.city).add("" + this.zipCode).toString().replace(' ', '+') +
                "&key=" + GOOGLEKEY;
        URL url = new URL(workingURL);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        Document doc = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(connection.getInputStream());
        NodeList nodes = doc.getElementsByTagName("location");
        StringBuilder res = new StringBuilder();
        for(int i = 0; i < nodes.getLength(); i++) {
            res.append(nodes.item(i).getTextContent().trim());
        }
        return res.toString().replaceFirst("\\s+", ",");
    }

}
