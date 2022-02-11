import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class musicButton extends button{
    int n;
    music m = new music();
    public void makeWindow(String textt){
        JFrame frame = new JFrame();

        Object[] options = {"Yes, please",
                    "No way!"};
        n = JOptionPane.showOptionDialog(frame,
            textt,
            "A Silly Question",
            JOptionPane.YES_NO_OPTION,
            JOptionPane.QUESTION_MESSAGE,
            null,     //do not use a custom Icon
            options,  //the titles of buttons
            options[0]); //default button title
        if (n == 0) {
            makeWindow("Random genre of music:" + m.retAns());
        }
    }
    public void display(){
        makeWindow("Random genre of music:" + m.retAns());
    }
}
