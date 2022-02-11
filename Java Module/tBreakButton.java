import java.awt.*;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.Timer;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class tBreakButton extends button{
    
    public static void addmainWindow(Container pane) {
        JLabel label = new JLabel();

	    pane.setLayout(new GridBagLayout());
	    GridBagConstraints c = new GridBagConstraints();

	    c.fill = GridBagConstraints.HORIZONTAL;
	    c.ipady = 40;      //make this component tall
	    c.weightx = 0.0;
	    c.gridwidth = 3;
	    c.gridx = 0;
	    c.gridy = 0;
	    pane.add(label, c);
        tBreak breakT = new tBreak();
        Timer timer = new Timer(500, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(breakT.isDone()){
                    label.setText("break over!");
                }
                else{
                    label.setText((breakT.timeLeft()+1) +" Minutes left");
                }
            }
          });
          timer.setRepeats(true);
          timer.setCoalesce(true);
          timer.setInitialDelay(0);
          timer.start();
    }
    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("GridBagLayoutDemo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Set up the content pane.
        addmainWindow(frame.getContentPane());


        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }
    public void display(){
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}
