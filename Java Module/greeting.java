public class greeting extends infoHolder{
    String[] greetings = {"Good Morning", "Good Afternoon", "Good Evening", "It's a little late isn't it?"};
    timeKeeper tTime = new timeKeeper();
    public String retAns(){
        if(tTime.getTime().getHour() <= 10){
            return greetings[0];
        }
        else if(tTime.getTime().getHour() <= 17){
            return greetings[1];
        }
        else if(tTime.getTime().getHour() <= 22){
            return greetings[2];
        }
        else{
            return greetings[3];
        }
    }
}
