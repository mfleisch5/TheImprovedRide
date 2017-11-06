import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Created by michaelfleischmann on 11/5/17.
 */
public class testAddress {
    Address a = new AddressImpl(160, "S 2nd St", "Brooklyn", 11211);

    @Test
    public void testGeoCode() throws Exception {
        assertEquals(a.getGeoCode(), "40.7127260,-73.9614129");
    }
}
