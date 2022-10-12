public class Birthday {

    //notes
    //the purpose of this program is to create a simulation
    //of 'The Birthday Problem'. This specific thought and
    //math experiment examines the question: How many people
    //need to enter a room until there are two people with the
    //same birthday in the room.
    //An interesting question that follows this premise is:
    //"What if we only let people in the room who were born
    //in January?" From here we have the basis for our program:
    //we take a command line argument of how many birthdays we
    //will consider as valid (366, for example, if we want to
    //allow for any birthday including feb 29), and another
    //command line argument to determine how many iterations
    //of our simulation we want to run.
    //We then run our program and print the distribution of
    //our results.


    public static void main(String[] args)
    {
        //initializes variables with command line arguments
        //and constants
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        int[] birthdays = new int[n + 1];
        int[] table_1 = new int[n + 2];
        double[] table_2 = new double[n + 2];
        int attempt_random = 0;
        int attempt = 0;
        boolean table_cutoff = false;
        String[] to_print = new String[3];

        //uses a for loop to create a random birthday in the 
        //specified range and adds 1 to the 'birthdays' array
        //at the index of the specified index until two of the
        //same birthdays are generated
        //the outermost loop repeats this process for the given
        //number of trials
        for (int i1 = 0; i1 < trials; i1++){
            attempt = 0;
            for (int i2 = 0; i2 < 1;){
                attempt_random = (int)Math.ceil(Math.random() * (n));
                i2 = birthdays[attempt_random];
                birthdays[attempt_random] = 1;
                attempt++;
            }
            table_1[attempt] += 1;
            table_2[attempt] += 1;
            birthdays = new int[n + 1];
        }

        //creates a sum of the values for the final output
        for (int i3 = 1; i3 <= n; i3++){
            table_2[i3] += table_2[i3 - 1];
        }

        //uses a for loop and string formatting to print the
        //final output of the program. The output of the
        //program ends when we have accounted for at least
        //50% of the trials
        System.out.println("\npeople      frequency:  %of attempts");
        System.out.println("entered:                represented:\n");
        for (int i4 = 1; table_cutoff != true; i4++){
            to_print[0] = String.format("%-12s", i4);
            to_print[1] = String.format("%-12s", table_1[i4]);
            to_print[2] = String.format("%-12s", table_2[i4] / (double)trials);
            System.out.println(to_print[0]+to_print[1]+to_print[2]);

            table_cutoff = ((table_2[i4] / (double)trials) >= 0.5);
        }
        System.out.print("\n");
    }
}