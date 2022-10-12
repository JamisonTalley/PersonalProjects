//imports libraries to read files and user input
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Wordle
{

    //creates a function to use information from previous guesses
    //to narrow the list of possible words for future guesses.
    //this is done by taking the the array of all five letter words,
    //and comparing it to the arrays that have been created to store
    //whether or not a letter is in the word, and if so, what position
    //could it belong to. Every word that doesn't agree with those
    //conditions is replaced with "XXXXX". Denoting that it is not a
    //valid guess. Finally we return that array containing all five
    //letter words and all of the invalid guesses changed to "XXXXX".
    public static String[] reduce(
        String[] words, char[] letters, char[] confirmed,
        char[] whitelist, char[] blacklist, char[][] yellowlist)
    {
        boolean kill_word = false;
        int check_word = 1;
        for (int i1 = 0; i1 < words.length; i1++){
            kill_word = false;
            check_word = ((!words[i1].equals("XXXXX")) ? 1 : 0);
            for (int i2 = 0; i2 < check_word; i2++){
                for (int i3 = 0; i3 < 26; i3++){
                    kill_word = (kill_word || 
                    words[i1].contains(String.valueOf(blacklist[i3])));
                }
                for (int i4 = 0; i4 < 26; i4++){
                    kill_word = (kill_word || 
                    (!(words[i1].contains(String.valueOf(whitelist[i4])))
                    && (whitelist[i4] != 0)));
                }
                for (int i5 = 0; i5 < 5; i5++){
                    kill_word = ((kill_word) ||
                    ((words[i1].charAt(i5) != (confirmed[i5])) &&
                    (confirmed[i5] != 0)));
                }
                for (int i6 = 0; i6 < 5; i6++){
                    for (int i7 = 0; i7 < 30; i7++){
                        kill_word = ((kill_word) ||
                        ((words[i1].charAt(i6) == (yellowlist[i6][i7]))));
                    }
                }
                if (kill_word) words[i1] = "XXXXX";
            }
        }
        return words;
    }

    //creates a function to cycle through a list of five letter
    //words, and pick the first one that is not denoted as invalid
    //by "XXXXX"
    public static char[] new_guess(
        String[] words, char[] test)
    {

        for (int i1 = 0; i1 < words.length; i1++){
            if (((!words[i1].equals("XXXXX")) &&
            (!(words[i1].toCharArray().equals(test))))){
                test = words[i1].toCharArray();
                i1 = words.length;
            }
        }
        return test;
    }


    //creates the main function for the program
    public static void main(String[] args){

        //creates an array of strings to hold every five letter
        //word. Note that the length of this array is very important
        //attempting to use a list of words of a different length
        //will likely break the program
        String[] words = new String[5757];
        //uses java.io.File to fill the 'words' array with the 
        //data from a file in the current directory named "words.txt".
        try{
            File text = new File("words.txt");
            Scanner list_reader = new Scanner(text);
            int words_counter = 0;
            while (list_reader.hasNextLine()){
                words[words_counter] = list_reader.nextLine();
                words_counter++;
            }
            list_reader.close();
        }
        catch (FileNotFoundException e){
            System.out.println("An error occurred.");
            e.printStackTrace();
        }


        //initializes variables to be used in the main function
        Scanner user_input = new Scanner(System.in);
        String word_color = "";
        char[] letters = {'a','b','c','d','e','f',
        'g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z'};
        char[] test = {'s','t','a','r','e'};
        char[] test_2 = {'l','i','n','g','o'};
        char[] confirmed = new char[5];
        char[] whitelist = new char[30];
        char[] blacklist = new char[30];
        char[][] yellowlist = new char[5][30];
        int guess_counter = 0;
        int confirmed_counter = 0;
        int whitelist_counter = 0;
        int blacklist_counter = 0;
        int yellowlist_counter = 0;
        boolean greyed_out = false;

        //uses a for loop to cycle through six attempts in a Wordle game
        //ends the program early if we get the correct word
        for (int i1 = 0; (i1 < 6) && (confirmed_counter < 5); i1++){
            //prints the guess for the current turn
            for (int i2 = 0; i2 < 5; i2++){
                System.out.print(test[i2]);
            }

            //promts the user to input the color coding from the Wordle
            //output for each letter of the guess
            for (int i3 = 0; i3 < 5; i3++){
                System.out.print("\nWhat color was letter "+(i3 + 1)+"?");
                System.out.print(" (grey, yellow, or green)\n");
                word_color = user_input.nextLine();


                //for grey words, we have two options. Either the letter
                //is not in the word, or the letter is a duplicate of a 
                //correct letter in our current guess. In the first case,
                //we simply add the letter to an array of chars called
                //'blacklist'. This simply holds every letter we know to
                //not be in the answer. In the second case, we add the
                //letter to a 2d array of characters called 'yellowlist'.
                //This 5x30 array stores all of the location and value of
                //ever letter that in the answer, but not the right spot.
                if (word_color.equals("grey")){
                    greyed_out = false;
                    for (int i4 = 0; i4 < 5; i4++){
                        if (test[i3] == confirmed[i4])greyed_out = true;
                    }
                    for (int i5 = 0; i5 < 30; i5++){
                        if (test[i3] == whitelist[i5])greyed_out = true;
                    }
                    if (!greyed_out){
                        blacklist[blacklist_counter] = test[i3];
                        blacklist_counter++;
                    }
                    else{
                        yellowlist[i3][yellowlist_counter] = test[i3];
                        yellowlist_counter++;
                    }
                }

                //If the letter is yellow, we add it to the afformentioned
                //'yellowlist' and a 1d char array called 'whitelist', where
                //we store every letter that we know to be in the word.
                //(Note, duplicates are allowed in all three of our char arrays)
                else if (word_color.equals("yellow")){
                    whitelist[whitelist_counter] = test[i3];
                    whitelist_counter++;
                    yellowlist[i3][yellowlist_counter] = test[i3];
                    yellowlist_counter++;
                }

                //If the letter is green, we first make sure that the
                //position in our 'confirmed' char array is not filled.
                //If we have a new green letter, we add it to its respective
                //location in our answer. We also add it to 'whitelist' for
                //the case where a letter appears as green before it apears 
                //as yellow
                else if ((word_color.equals("green"))){
                    if (confirmed[i3] != test[i3]){
                        confirmed[i3] = test[i3];
                        confirmed_counter++;
                        whitelist[whitelist_counter] = test[i3];
                        whitelist_counter++;
                    }
                }

                //repeats the process if an invalid user input is given.
                else{
                    System.out.println("not a valid color, try again");
                    i3--;
                }

                //handles the situation where the Worlde game denotes a
                //letter as grey when it is in the answer
                for (int i6 = 0; i6 < 30; i6++){
                    for (int i7 = 0; i7 < 5; i7++){
                        if ((blacklist[i6] == confirmed[i7]) &&
                            (blacklist[i6] != 0)){
                            for (int i8 = 0; i8 < 5; i8++){
                                if (i8 != i7){
                                    yellowlist[i8][yellowlist_counter] =
                                    blacklist[i6];
                                    yellowlist_counter++;
                                }
                            }
                            blacklist[i6] = 0;
                        }
                    }
                }
            }

            //calls the reduce funciton to limit possible guesses using
            //the above parameters
            words = reduce(words, letters, confirmed,
            whitelist, blacklist, yellowlist);

            //uses a pre-determined guess for the second iteration,
            //and uses the new_guess function for all successive
            //iterations
            if (i1 == 0){
                test = test_2;
            }
            else{
                test = new_guess(words, test);
            }
            System.out.print("\n");
            guess_counter++;

        }
        user_input.close();

        //prints an end screen for the Wordle
        if (confirmed_counter > 4){
            System.out.println("Answered in "+guess_counter+" guesses!");
        }
        else System.out.println("Wordle Failed :(");
    }
}