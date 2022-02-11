import java.lang.Math;
public class music extends infoHolder{
    String[] music = {"Pop", "Rock", "Lo-fi", "Video Game"};
    public String retAns(){
        return randomMusic();
    }
    private String randomMusic(){
        int index = (int)(Math.random() * music.length);
        return music[index];
    }
}
