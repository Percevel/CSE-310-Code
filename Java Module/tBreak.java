import java.time.LocalTime;
import static java.time.temporal.ChronoUnit.MINUTES;

public class tBreak{
    String ans;
    LocalTime end;
    timeKeeper timeK = new timeKeeper();
    public tBreak(){
        startTimer();
    }
    public void startTimer(){
        end = timeK.getTime().plusMinutes(30);
        System.out.println(end);
    }
    public long timeLeft(){
        return timeK.getTime().until(end, MINUTES);
    }
    public boolean isDone(){
        return timeK.isOver(timeK.getTime(), end);
    }
}
