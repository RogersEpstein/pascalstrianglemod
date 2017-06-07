import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class PascalsTriangle {

	public PascalsTriangle(){
		JFrame frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		PTGUI golgui = new PTGUI();
		frame.getContentPane().add(golgui.display());
		frame.pack();
		frame.show();
	}
	
	public static void main(String[] args){
		PascalsTriangle pt = new PascalsTriangle();
	}
	
	protected class PTGUI {
		
		JPanel panel;
		int[][] values;
		JLabel[][] grid;
		Color[] colors;
		
		final int GRID_SIZE = 300;
		final int TILE_SIZE = 3;
		final int COLORS = 8;
		
		public PTGUI(){
			//Color[] dummy = {Color.black, Color.white, Color.red, Color.yellow, Color.blue, Color.green, Color.magenta, Color.cyan, Color.gray};
			Color[] dummy = {Color.black, Color.white, Color.white, Color.white, Color.white, Color.white, Color.white, Color.white, Color.white};
			colors = dummy;
			panel = new JPanel();
			panel.setLayout(null);
			panel.setPreferredSize(new Dimension(20 + GRID_SIZE * TILE_SIZE, 20 + GRID_SIZE * TILE_SIZE));
			panel.setBackground(colors[0]);
			grid = new JLabel[GRID_SIZE][GRID_SIZE];
			values = new int[GRID_SIZE][GRID_SIZE];
			for (int i = 0; i < GRID_SIZE; i += 1){
				for (int j = 0; j < GRID_SIZE; j += 1){
					grid[i][j] = new JLabel();
					grid[i][j].setOpaque(true);
					grid[i][j].setSize(TILE_SIZE, TILE_SIZE);
					grid[i][j].setLocation(10 + j*TILE_SIZE, 10 + i*TILE_SIZE);
					if (j == 0){
						values[i][j] = 1;
					} else if (i == 0){
						values[i][j] = 0;
					} else {
						values[i][j] = (values[i-1][j] + values[i-1][j-1]) % COLORS;
					}
					grid[i][j].setBackground(colors[values[i][j]]);
					panel.add(grid[i][j]);
				}
			}
		}
		
		public JPanel display(){
			return panel;
		}
	}
}
