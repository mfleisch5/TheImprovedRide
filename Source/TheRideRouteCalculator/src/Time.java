public class Time implements Comparable<Time>{

    public Time(String am_pm, int hour, int minutes) {

        this.am_pm = am_pm;
        this.hour = hour;
        this.minutes = minutes;
    }
    private String am_pm;
    private int hour;
    private int minutes;

    //negative if given is less than
    @Override
    public int compareTo(Time t) {
        if(this.am_pm.equals(t.am_pm)) {
            if(this.hour < t.hour || this.minutes < t.minutes) {
                return 1;
            }
            if (this.hour == t.hour && this.minutes == t.minutes) {
                return 0;
            }
            else return -1;
        }
        else if (this.am_pm.equals("AM")){  //this time comes before given time
            return 1;
        } else return -1; //given time comes before this time.
    }

    public int getHour(){return this.hour;}
    public String getAm_pm() {return this.am_pm;}
    public int getMinutes() {return this.minutes;}

}
