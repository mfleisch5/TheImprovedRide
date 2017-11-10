import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Created by michaelfleischmann on 11/5/17.
 */
public class testAddress {
    Address brooklyn = new AddressImpl(277, "Bedford Ave", "Brooklyn", 11211);
    Address ohio = new AddressImpl(25774, "Tricia Dr", "Westlake", 44145);

    @Test
    public void testGeoCode() throws Exception {
        assertEquals(brooklyn.getGeoCode(), "40.7142205,-73.9612903");
        assertEquals(ohio.getGeoCode(), "41.4468986,-81.9004179");
    }
}
