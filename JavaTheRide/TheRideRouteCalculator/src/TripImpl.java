/**
 * An implementation of a trip.
 */
public class TripImpl implements Trip {

    //************DO NOT IMPLEMENT THESE UNTIL UNIT TESTS HAVE BEEN CREATED************

    public TripImpl(int tripId, boolean subscription, boolean ada, boolean anchor, String requestTime,
                 int numPca, int numCompanions, boolean serviceAnimal, Address pickup, Address dropoff, int rideID) {
        this.tripID = tripId;
        this.subscription = subscription;
        this.ada = ada;
        this.anchor = anchor;
        this.requestTime = requestTime;
        this.numPca = numPca;
        this.numCompanions = numCompanions;
        this.serviceAnimal = serviceAnimal;
        this.pickup = pickup;
        this.dropoff = dropoff;
        this.rideID = rideID;
    }

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
    private int rideID;

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

    @Override
    public int getRideID() {
        return 0;
    }
}
