import java.awt.*;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class mainWindow extends JPanel{
    

    public static void addmainWindow(Container pane) {
        JButton b1, b2, b3;
        JLabel label;
        greeting greet = new greeting();
        timeKeeper timeK = new timeKeeper();

	    pane.setLayout(new GridBagLayout());
	    GridBagConstraints c = new GridBagConstraints();
    
	    b1 = new JButton("Random Music");
	    c.fill = GridBagConstraints.HORIZONTAL;
	    c.weightx = 0.5;
	    c.gridx = 0;
	    c.gridy = 1;
        b1.setActionCommand("music");
	    pane.add(b1, c);

        b2 = new JButton("Motivation");
	    c.fill = GridBagConstraints.HORIZONTAL;
	    c.weightx = 0.5;
	    c.gridx = 2;
	    c.gridy = 1;
        b2.setActionCommand("motivation");
	    pane.add(b2, c);

        b3 = new JButton("Break Time");
	    c.fill = GridBagConstraints.HORIZONTAL;
	    c.weightx = 0.5;
	    c.gridwidth = 3;
	    c.gridx = 0;
	    c.gridy = 2;
        b3.setActionCommand("breakTime");
	    pane.add(b3, c);

        label = new JLabel(greet.retAns());
	    c.fill = GridBagConstraints.HORIZONTAL;
	    c.ipady = 40;      //make this component tall
	    c.weightx = 0.0;
	    c.gridwidth = 3;
	    c.gridx = 0;
	    c.gridy = 0;
	    pane.add(label, c);


        b1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
                {
                    if("music".equals(e.getActionCommand())){
                        musicButton b = new musicButton();
                        b.display();
                    }
                }
        });
        b2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
                {
                    if("motivation".equals(e.getActionCommand())){
                        motivationButton b = new motivationButton();
                        b.display();
                    }
                }
        });
        b3.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
                {
                    if("breakTime".equals(e.getActionCommand())){
                        tBreakButton b = new tBreakButton();
                        b.display();
                    }
                }
        });
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

    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}