public class Minesweeper {
    //notes
    //The goal of this program is to generate a field
    //of mines in accordance with the structure of the
    //game "Minesweeper". This is meant to serve as an
    //introduction to the game of minesweeper for a beginner
    //to better understand the structure of the game, as
    //mines are exposed by default

    //the challenge I set for this program was to write
    //entirely non-branching and optomized code. The primary
    //purpose behind this goal is performance, as non branching
    //code with linear performace optomization runs much faster.
    //An unfortunate side effect of this, however, is a decrease
    //in readability. To combat this, I included detailed 
    //documentation for this program, but basic knowledge of
    //non-branching code structures in Java will be necessary
    //to follow this program.

    public static void main(String[] args)
    {
        //Initializes variables from command line arguments
        //and initializes variables for use in the program
        
        int rows = Integer.parseInt(args[0]);
        int collumns = Integer.parseInt(args[1]);
        int mines = Integer.parseInt(args[2]);
        int size = rows * collumns;
        int row = 0;
        int collumn = 0;
        int rnd = 0;
        int row_opp = -1;
        int col_opp = -1;
        boolean close_valid = true;
        String[] map = new String[size + 1];
        int[] mine_map = new int[size];
        int[][] num_map = new int[rows][collumns];
        int[][] close_mine = {{-1, -1, -1,  0, 0, 0,  1, 1, 1, -1},
                              {-1,  0,  1, -1, 0, 1, -1, 0, 1, -1}};

        //generates the location of the mines
        for (int i1 = 0; i1 < mines; i1++){
            rnd = (int)Math.rint(Math.random() * (size - 1));
            i1 -= ((mine_map[rnd] == 1) ? 1 : 0);
            mine_map[rnd] += ((mine_map[rnd] == 0) ? 1 : 0);
        }

        //uses a for loop to iterate through each position in the grid
        for (int i2 = 0; (i2 < size); i2++){
            row = Math.floorDiv(i2, collumns);
            collumn = i2 % collumns;

            //uses a for loop to add 1 to each of the spaces
            //surrounding a mine
            for (int i3 = 0; (i3 < 9); i3++){
                row_opp = close_mine[1][i3];
                col_opp = close_mine[0][i3];
                //uses boolean logic instead of an if looop
                //to prevent branching
                close_valid = (0 <= (row + row_opp)) &&
                ((row + row_opp) < rows) && ((0 <= (collumn + col_opp))) &&
                ((collumn + col_opp) < collumns) && (mine_map[i2] == 1);

                for (;(close_valid == true);){
                    num_map[row + row_opp][collumn + col_opp] += 1; 
                    close_valid = false;
                }
            }
        }

        //uses a for loop to fill the "map" array that we
        //will print out as the final output
        for (int i4 = 0; i4 < size; i4++){
            row = Math.floorDiv(i4, collumns);
            collumn = i4 % collumns;
            map[i4] = String.valueOf(num_map[row][collumn]);
            //replaces each mine with a star
            for (int i5 = 0; (i5 < 1) && (mine_map[i4] == 1); i5++){
                map[i4] = "*";
            }
            System.out.print(map[i4]+"  ");
            for (int i6 = 0; (i6 < 1) && (collumn == (collumns - 1)); i6++){
                System.out.print("\n");
            }
        }
        System.out.println();
    }
}

//extras

//number of rows, collumns and mines
//calculates the size of the grid
//'row' and 'collumn' are counting variables
//used in loops to hold the location on the grid
//'rnd' is the variable we will use to calculate
//a random integer for our mine placement
//'row_opp' and 'col_opp' are variables that will
//help us add 1 to a 3x3 square around the mine locations
//'close_valid' is a variable for error management that
//makes sure the locations we want to access around a mine
//exist in the num_map array
//'map' is the final output array for the program
//'mine_map' is the array in which we generate the mines
//'num_map' is the 2D array where we store the number of
//adjacent mines for each location on the grid
//'close_mine' is a reference array we will use to 
//detail instructions for future for loops in order
//to decrease code clutter
//the first loop generates the location of the mines
//into the list 'mine_map'\