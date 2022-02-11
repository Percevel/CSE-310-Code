import java.lang.Math;
public class motivation extends infoHolder{
    String[] motivation = {"Nothing is impossible. The word itself says ‘I’m possible!",
                    "There is nothing impossible to they who will try.",
                    "The bad news is time flies. The good news is you’re the pilot.",
                    "Life has got all those twists and turns. You’ve got to hold on tight and off you go."};
    public String retAns(){
        return randomMotivation();
    }
    private String randomMotivation(){
        int index = (int)(Math.random() * motivation.length);
        return motivation[index];
    }
}
