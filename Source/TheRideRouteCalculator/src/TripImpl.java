/**
 * An implementation of a trip.
 */
public class TripImpl implements Trip {

    private int tripID;
    private boolean subscription;
    private boolean ada;
    private boolean anchor;
    private String requestTime;
    private int numPca;
    private int numCompanions;
    private boolean serviceAnimal;
    private Address pickup;
    private Address dropoff;

    @Override
    public int getTripID() {
        return 0;
    }

    @Override
    public boolean getSubscription() {
        return false;
    }

    @Override
    public boolean getADA() {
        return false;
    }

    @Override
    public boolean getAnchor() {
        return false;
    }

    @Override
    public String getRequestTime() {
        return null;
    }

    @Override
    public int getPcas() {
        return 0;
    }

    @Override
    public int getCompanions() {
        return 0;
    }

    @Override
    public boolean getServiceAnimal() {
        return false;
    }

    @Override
    public Address getPickup() {
        return null;
    }

    @Override
    public Address getDropoff() {
        return null;
    }
}
