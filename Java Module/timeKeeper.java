import java.time.LocalTime;  

public class timeKeeper{

    public String getCurrentTime(){
        LocalTime current = LocalTime.now();
        String ret = current.getHour() + ":" + current.getMinute();
        return ret;
    }

    public LocalTime getTime(){
        LocalTime current = LocalTime.now();
        return current;
    }
    
    public boolean isOver(LocalTime present, LocalTime future){
        if(future.compareTo(present) <= 0){
            return true;
        }
        return false;
    }
}